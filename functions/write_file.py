import os

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