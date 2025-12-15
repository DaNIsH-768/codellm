import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file with optional arguments using subprocess. The python file needs to be in the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the python file to execute. If the file path is invalid or is not a python file an error is thrown.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="The optional arguments to call the file with.",
                items=types.Schema(  # <--- MUST be present for type=ARRAY
                    type=types.Type.STRING # <--- Defines the type of each item in the array (e.g., ["arg1", "arg2"])
                ),
            ),
        },
    ),
)

def run_python_file(working_directory, file_path, args=[]):
    working_directory_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))

    if not target_file.startswith(working_directory_abs):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'
    
    if not target_file.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        process_obj = subprocess.run(['python3', target_file, *args], timeout=30, capture_output=True)
        if process_obj.stdout == '':
            return 'No output produced'
        
        output = f'STDOUT: {process_obj.stdout}\nSTDERR: {process_obj.stderr}'

        if process_obj.returncode != 0:
            output += f'\nProcess exited with code {process_obj.returncode}'

        return output
    
    except Exception as e:
        return f"Error: executing Python file: {e}"





