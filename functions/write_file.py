import os
from google import genai
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path","content"],
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="Dworking directory to work from, default is current directory",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="file path relative to the working directory."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to file"
            )
        },
    ),
)

def write_file(working_directory, file_path, content):
    if working_directory == None:
        working_directory = "."
    
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
    except Exception as e:
        return f'    Error: an error occured: {e}'

    if valid_target_dir == False:
        return f'    Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if os.path.isdir(target_path):
        return f'    Error: Cannot write to "{file_path}" as it is a directory'

    

    try:
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        with open(target_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'    Error: an error occured when writing to file {file_path}: {e}'