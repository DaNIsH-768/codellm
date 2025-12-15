import os
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Provides the content in the specified file. ",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to read content from, relative to the working directory. If file path is invalid returns an error.",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):
    MAX_CHARS = 10000
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    
    try:
        if not target_file.startswith(working_dir_abs):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
    except:
        return 'Error: os module function execution failed'

    with open(target_file, 'r', encoding='utf-8') as f:
        file_content_str = f.read()
        if len(file_content_str) > MAX_CHARS:
            return f"{len(file_content_str)} [...File '{file_path}' truncated at 10000 characters]"

        return file_content_str
    


    

    