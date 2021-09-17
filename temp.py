import os


def rename_current_dir(folder):
    for root, directories, filenames in os.walk(folder):
        for directory in directories:
            print(os.path.join(root, directory))
            print(directory)
        break


def rename_sub_dir(folder):
    for root, directories, filenames in os.walk(folder):
        for directory in directories:
            print(os.path.join(root, directory))
            print(directory)


def rename_current_dir_files(folder):
    for root, directories, filenames in os.walk(folder):
        for filename in filenames:
            print(os.path.join(root, filename))
        break


def rename_sub_dir_files(folder):
    for root, directories, filenames in os.walk(folder):
        for filename in filenames:
            print(os.path.join(root, filename))


lib = 'C:\\Users\\tejas\\Documents\\MEGA\\library - copy'

rename_current_dir(lib)
# rename_sub_dir(lib)
# rename_current_dir_files(lib)
# rename_sub_dir_files(lib)
