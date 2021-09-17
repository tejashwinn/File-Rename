import os
from os import listdir
from os.path import isfile, join

# global variables
HELP = '-h'
QUIT = '-q'
ALL_OPTIONS = ('-h', '-q', '-f', '-s', '-n', '-r', '-a', '-ra', '-c', 'su')


def read_directory(current_dir=os.getcwd()):
    onlyfiles = [f for f in listdir(current_dir) if isfile(join(current_dir, f))]
    print(onlyfiles)


def final_rename(old, new, extension):
    pass


def extension(arr):
    pass


def check_existing(filename):
    pass


def swap_char(all_existing_files, new, old):
    pass


def menu(split_values):
    if split_values[0] == ALL_OPTIONS[0]:
        helpFunc()
    elif split_values[0] == ALL_OPTIONS[1]:
        print('Exiting...')
        exit()
    elif split_values[0] == ALL_OPTIONS[2]:
        # move_to_destination(split_values[1])
        print('Not yet developed')
    # swap characters
    elif split_values[0] == ALL_OPTIONS[3]:
        pass
    elif split_values[0] == ALL_OPTIONS[4]:
        helpFunc()
    elif split_values[0] == ALL_OPTIONS[5]:
        helpFunc()
    elif split_values[0] == ALL_OPTIONS[6]:
        helpFunc()
    elif split_values[0] == ALL_OPTIONS[7]:
        helpFunc()
    elif split_values[0] == ALL_OPTIONS[8]:
        helpFunc()
    else:
        print('Ran into errors')


def renameFunc(argc):
    if argc == HELP:
        helpFunc()
    elif argc == QUIT:
        print('Exiting...')
        exit()
    else:
        split_values = argc.split(' ')
        if split_values[0] in ALL_OPTIONS:
            menu(split_values)
        else:
            print('Wrong Options')


def helpFunc():
    print('q: quit')
    print('f: folder in different location(Not yet developed)')
    print('s: swap characters')
    print('n: numerical naming')
    print('r: random num naming')
    print('a: random alpha naming')
    print('ra: random alpha-num naming')
    print('c: custom format')
    print('S: to rename subdirectories')


# start
while True:
    print('\ntry: \n\t-h for help\n\t-c for custom format\n\t-q to quit')
    user_input = input()
    renameFunc(user_input.strip())
