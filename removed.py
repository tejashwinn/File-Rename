# dir_dict = {}
# file_dict = {}
#
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
#     for (dir_path, dir_names, file_names) in walk(current):
#         files_current_dir.extend(file_names)
#         break
#     file_dict[current] = files_current_dir
#
#
#     if split_values[0] == ALL_OPTIONS[0]:
#         helpFunc()
#     elif split_values[0] == ALL_OPTIONS[1]:
#         print('Exiting...')
#         exit()
#     elif split_values[0] == ALL_OPTIONS[2]:
#         # move_to_destination(split_values[1])
#         print('Not yet developed')
#     # swap characters
#     elif split_values[0] == ALL_OPTIONS[3]:
#         pass
#     elif split_values[0] == ALL_OPTIONS[4]:
#         helpFunc()
#     elif split_values[0] == ALL_OPTIONS[5]:
#         helpFunc()
#     elif split_values[0] == ALL_OPTIONS[6]:
#         helpFunc()
#     elif split_values[0] == ALL_OPTIONS[7]:
#         helpFunc()
#     elif split_values[0] == ALL_OPTIONS[8]:
#         helpFunc()
#     else:
#         print('Ran into errors')