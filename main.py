import os
import subprocess
import shlex

# Made in python, with pycharm
# thanks for green1490#2863 for helping me with arguments

print('Termithon')
idkdwij = '''
    I   D       K   K   D       W         W     I       J
    I   D   D   K K     D  D    W    W    W     I   J   J
    I   D       K   K   D       W  W   W  W     I     J J
'''
print('The Python based terminal by' + idkdwij + 'it says idkdwij')
print('The source is here')


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


current_dir = os.getcwd()

commands = '''ls (shows files in current directory)
exit (exits program)
'''


def cdCmd():
    print("sorry, the cd command doesnt update so no ")
    main()
    '''
    path = input('Directory: ')
    if os.path.isdir(path) == True:
        current_dir = args
        global new_current_dir
        new_current_dir = args
        global newcurrdir
        newcurrdir = True
        main()
    else:
        print('wrong directory')
        main()
        '''


def whatiscommand():
    if cmd == 'help':
        print(commands)
        main()

    elif cmd == 'ls':
        print(os.listdir(current_dir))
        main()

    elif cmd == "cd":
        global args
        args = cmd
        cdCmd()
    elif cmd == 'exit':
        exit()
    else:
        print('invalid')
        main()


def main():
    global cmd
    cmd = input(current_dir + '>')
    whatiscommand()


lsdir = current_dir
main()
