dir_dict = {}
file_dict = {}

def iterator_dirs(current):
    for root, directories, filenames in os.walk(current):
        for directory in directories:
            files = [f for f in listdir(os.path.join(root, directory))
                     if isfile(join(os.path.join(root, directory), f))]
            dir_dict[os.path.join(root, directory)] = files


def iterator_files(current):
    files_current_dir = []
    for (dir_path, dir_names, file_names) in walk(current):
        files_current_dir.extend(file_names)
        break
    file_dict[current] = files_current_dir
