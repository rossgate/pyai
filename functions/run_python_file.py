import os, subprocess

from google import genai
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute python files with optional arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["working_directory","file_path"],
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="Working directory path to run python files from",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="file path relative to the working directory."
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="list of args to pass into python file.",
                items=types.Schema(
                    type=types.Type.STRING,
                    description="arg item"
                )
            )
        },
    ),
)

def run_python_file(working_directory, file_path, args=None):
    if working_directory == None or working_directory == "":
        working_directory = "."

    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
    except Exception as e:
        return f'   Error: an error occured: {e}'

    if valid_target_dir == False:
        return f'   Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(target_path) or not os.path.isfile(target_path):
        return f'   Error: "{file_path}" does not exist or is not a regular file'

    if not file_path.endswith('.py'):
        return f'   Error: "{file_path}" is not a Python file'

    

    return_string = ""
    try:
        command = ["python", target_path]
        if args != None:
            command.extend(args)

        completed_process = subprocess.run(
            command, 
            cwd=working_dir_abs,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, 
            text=True, 
            timeout=30
            )
      
        if completed_process.returncode != 0:
            return f'Process exited with code {completed_process.returncode}'
        if completed_process.stdout == None or completed_process.stderr == None:
            return f'No output produced'
        
        return_string += f'STDOUT: {completed_process.stdout}, STDERR: {completed_process.stderr}'
        
        return return_string

    except Exception as e:
        return f'   Error: "error executing python file: {file_path}: {e}'