import os, subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
    except Exception as e:
        return f'   Error: an error occured: {e}'

    if valid_target_dir == False:
        return f'   Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_path):
        return f'   Error: "{file_path}" is not a Python file'

    return_string = ""
    try:
        command = ["python", target_path]
        if args != None:
            command.extend(args)

        completed_process = subprocess.run(command, stdout=True, stderr=True, text=True, timeout=30)

        if completed_process.returncode != 0:
            return f'Process exited with code X'
        if completed_process.stdout == None and completed_process.stderr == None:
            return f'No output produced'
        
        return_string += f'STDOUT: {completed_process.stdout}, STDERR: {completed_process.stderr}'
        
        return return_string

    except Exception as e:
        return f'   Error: "error executing python file: {file_path}: {e}'