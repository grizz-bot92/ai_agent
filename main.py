import os
import sys
from google import genai
from dotenv import load_dotenv
from google.genai import types
from call_functions import available_functions, call_function
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

try:
    for _ in range(20):
        response = client.models.generate_content(
            model='gemini-2.0-flash-001', 
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt),
        )

        function_calls = response.function_calls
        for candidate in response.candidates:
            messages.append(candidate.content)
        if function_calls:
            for function_call in function_calls:
                result = call_function(function_call)
                messages.append(result)
        elif response.text:
            print(f"Final response: {response.text}")
            break
            
except Exception as e:
    print(f"Error: {e}")




if "--verbose" in sys.argv:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

is_verbose = "--verbose" in sys.argv

if response.function_calls:
    for call in response.function_calls:
        function_call_result = call_function(call, is_verbose)
        try:
            function_call_result.parts[0].function_response.response
            if is_verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
        except Exception:
            raise Exception("Fatal Error")
else:
    print(response.text)


