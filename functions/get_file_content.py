import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    target_dir = os.path.abspath(full_path)
    abs_working_dir = os.path.abspath(working_directory) + os.sep

    try:
        if not target_dir.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_dir):
            return f'Error: File not found or is not a regular file: "{file_path}"'
    
        with open(target_dir, "r") as f:
            file_content_string = f.read()
        if len(file_content_string) > MAX_CHARS:
            return file_content_string[:MAX_CHARS] + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        else:
            return file_content_string
    except Exception as e:
        return f"Error: {e}"