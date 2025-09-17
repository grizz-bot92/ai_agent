import os
import sys
from google import genai
from dotenv import load_dotenv
from google.genai import types
from call_functions import available_functions
from prompts import system_prompt

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    print("Error, no prompt entered!")
    sys.exit(1)

prompt = sys.argv[1]

messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)])
]


response = client.models.generate_content(
    model='gemini-2.0-flash-001', 
    contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt),
)


if "--verbose" in sys.argv:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if response.function_calls:
    for call in response.function_calls:
        print(f'Calling function: {call.name}({call.args})')

else:
    print(response.text)


