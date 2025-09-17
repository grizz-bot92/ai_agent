import os
from google.genai import types

def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    target_dir = os.path.abspath(full_path)
    abs_working_dir = os.path.abspath(working_directory)

    try:
        if not target_dir.startswith(abs_working_dir):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        parent_dir = os.path.dirname(target_dir)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
        with open(target_dir, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Ability to write and overwrite files.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to write files to."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="the content that is written to the file"
            ),
        },
        required=["file_path", "content"],
    ),
)