import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)

    abs_path = os.path.abspath(full_path).rstrip(os.sep) + os.sep
    abs_working = os.path.abspath(working_directory).rstrip(os.sep) + os.sep
    
    if not abs_path.startswith(abs_working):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    try:
        lines = []

        for name in os.listdir(full_path):
            entry_path = os.path.join(full_path, name)
            is_dir = os.path.isdir(entry_path)
            size = os.path.getsize(entry_path)
            formatted_lines = f'- {name}: file_size={size} bytes, is_dir={is_dir}'
            lines.append(formatted_lines)
    
        return "\n".join(lines)
    
    except Exception as e:
            return f'Error: {e}'

