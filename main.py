import os
from os import listdir
from os.path import isfile, join

# global variables
HELP = '-h'
QUIT = '-q'
ALL_OPTIONS = ('-f', '-d', '-F', '-D', '-s', '-n', '-r', '-a', '-N', '-c')


def final_rename(filename):
    pass


def extension(arr):
    pass


def check_existing(filename):
    pass


def swap_char(all_existing_files, new, old):
    pass


def renameFunc(argc):
    if argc == HELP:
        helpFunc()
    elif argc == QUIT:
        print('Exiting...')
        exit()
    else:
        argc = argc.split(' ')
        if argc[0] and argc[1] in ALL_OPTIONS:
            menu(argc)
        else:
            print('options are wrong')


def menu(input_char):
    print(input_char)


def helpFunc():
    print('-q: quit application')
    print('-e: to exit help menu')
    print('Main:')
    print('\t-f: files in current directory')
    print('\t-d: directories in current directory')
    print('\t-F: files in sub directory')
    print('\t-D: All directories sub directories')

    print('Options:')
    print('\t-s: swap characters')
    print('\t-n: numerical naming')
    print('\t-r: random num naming')
    print('\t-a: random alpha naming')
    print('\t-N: random alpha-num naming')
    # todo
    print('\t-c: custom format ')

    value = input().lower()
    while value != '-e' or value != '-q':
        helpFunc()
    if value == '-e':
        return
    elif value == '-q':
        exit()


# start
while True:
    print('\n\t-h for help\n\t-q to quit\n')
    user_input = input()
    renameFunc(user_input.strip())
