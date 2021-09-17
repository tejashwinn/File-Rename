import os

# global variables
HELP = '-h'
QUIT = '-q'
ALL_OPTIONS = ('-h', '-q', '-f', '-s', '-n', '-r', '-a', '-ra', '-c')


def final_rename(old, new, extension):
    pass


def extension(arr):
    pass


def check_existing(filename):
    pass


def move_to_destination(location):
    pass


def menu(split_values):
    if split_values[0] == ALL_OPTIONS[0]:
        helpFunc()
    elif split_values[0] == ALL_OPTIONS[1]:
        print('Exiting...')
        exit()
    elif split_values[0] == ALL_OPTIONS[2]:
        move_to_destination(split_values[1])
    elif split_values[0] == ALL_OPTIONS[3]:
        helpFunc()
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
    print('f: folder in different location')
    print('s: swap characters')
    print('n: numerical naming')
    print('r: random num naming')
    print('a: random alpha naming')
    print('ra: random alpha-num naming')
    print('c: custom format')


# start
while True:
    print('\ntry: \n\t-h for help\n\t-c for custom format\n\t-q to quit')
    user_input = input()
    renameFunc(user_input.strip())
