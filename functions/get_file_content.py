import os
from config import *

def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
    except Exception as e:
        return f'    Error: an error occured: {e}'

    if valid_target_dir == False:
        return f'    Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(path=target_path):
        return f'    Error: File not found or is not a regular file: "{file_path}"'

    content = ""
    try:
        with open(target_path, "r") as f:
            content = f.read(CHARACTER_LIMIT)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {CHARACTER_LIMIT} characters]'
    except Exception as e:
        return f'   Error: an error occured: {e}'

    return content