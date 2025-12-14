import os
import subprocess

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





