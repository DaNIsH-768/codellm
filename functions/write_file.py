import os
import subprocess
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file. The file is constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write to. If the file path doesn't exist a new one is created.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file",
            ),
        },
    ),
)

def write_file(working_directory, file_path, content):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

    try:
        if not target_file.startswith(working_dir_abs):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    except:
        return 'Error: os module function error'

    parent_dirs = '/'.join(target_file.split('/')[:-1])
    if not os.path.exists(parent_dirs):
        os.makedirs(parent_dirs)
    
    with open(target_file, "w") as f:
        try:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except:
            return f'Error: writing to "{file_path}" failed.'