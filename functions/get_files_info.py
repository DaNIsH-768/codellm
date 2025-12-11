import os

def get_files_info(working_directory, directory='.'):
    path = os.path.join(working_directory, directory)
    #rint('path: ', path)
    if not os.path.isdir(path):
        return f'Error: "{directory}" is not a directory'

    complete_path = os.path.abspath(working_directory)
   #print('complete path:', complete_path)
    absolute_path = os.path.abspath(path)
    #print(absolute_path)
    if absolute_path.startswith(complete_path):
        dirs = os.listdir(absolute_path)
        #print(dirs)
        string = ''
        try:
            for d in dirs:
                new_path = os.path.join(absolute_path, d)
                string += f'- {d}: file_size={os.path.getsize(new_path)} bytes, is_dir={not os.path.isfile(new_path)}\n'
        except:
            return 'Error: Internal os function error'
        
        return string


    else:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'