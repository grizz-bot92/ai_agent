from google.genai import types
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.run_python_file import schema_run_python_file, run_python_file
from functions.write_file import schema_write_file, write_file

all_available_functions = {
     "get_files_info": get_files_info,
     "get_file_content": get_file_content,
     "run_python_file": run_python_file,
     "write_file": write_file,
}

def call_function(function_call_part, verbose=False):
     if verbose:
          print(f"Calling function: {function_call_part.name}({function_call_part.args})")
     else:
          print(f" - Calling function: {function_call_part.name}")
     
     if function_call_part.name not in all_available_functions:
          return types.Content(
               role="tool",
               parts= [
                    types.Part.from_function_response(
                         name=function_call_part.name,
                         response={"error": f"Unknown function: {function_call_part.name}"}
                    )
               ],
          )


     function_name = all_available_functions[function_call_part.name]
     function_call_part.args["working_directory"] = "./calculator" 
     function_result = function_name(**function_call_part.args)

     return types.Content(
          role="tool",
          parts=[
               types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": function_result}
               )
          ],
     )




available_functions = types.Tool(
     function_declarations=[
          schema_get_files_info,
          schema_get_file_content,
          schema_run_python_file,
          schema_write_file,

     ]
)