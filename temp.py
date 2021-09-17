import os
from os import listdir
from os.path import isfile, join
from os import walk

lib = 'C:\\Users\\tejas\\Documents\\MEGA\\library'

dir_dict = {}
file_dict = {}


# def iterator_dirs(current):
#     for root, directories, filenames in os.walk(current):
#         for directory in directories:
#             files = [f for f in listdir(os.path.join(root, directory))
#                      if isfile(join(os.path.join(root, directory), f))]
#             dir_dict[os.path.join(root, directory)] = files
#
#
# def iterator_files(current):
#     files_current_dir = []
#
#     for (dir_path, dir_names, file_names) in walk(current):
#         files_current_dir.extend(file_names)
#         break
#     file_dict[current] = files_current_dir
#
#
# iterator_dirs(lib)
# iterator_files(lib)

# for i in dir_dict:
#     print(i, dir_dict[i])
#
# for i in file_dict:
#     print(i, file_dict[i])


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


# iterator_dirs(lib)

for root, directories, filenames in os.walk(lib):
    for filename in filenames:
        print(os.path.join(root, filename))
    break

# print(f)
