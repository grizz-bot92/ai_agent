import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)
    target_dir = os.path.abspath(full_path)
    abs_working_dir = os.path.abspath(working_directory)

    try:
        if not target_dir.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(target_dir):
            return f'Error: File "{file_path}" not found.'

        if not target_dir.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        command_list = ["python", target_dir] + args
        completed_process = subprocess.run(args=command_list, timeout=30, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        stdout_str = completed_process.stdout.decode('utf-8').strip()
        stderr_str = completed_process.stderr.decode('utf-8').strip()
        final_output = []

        if stdout_str:
            final_output.append(f"STDOUT: {stdout_str}")
        if stderr_str:
            final_output.append(f"STDERR: {stderr_str}")
        if completed_process.returncode != 0:
            final_output.append(f"Process exited with code {completed_process.returncode}")
        if not final_output:
            return "No output produced"

        return "\n".join(final_output)
    
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="runs arbitrary python code inside the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute"
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional command-line arguments",
            ),
        },
        required=["file_path"],
    ),
)