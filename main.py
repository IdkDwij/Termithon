import os
import shlex
import socket
import getpass
# Made in python, with pycharm
# thanks for green1490#2863 for helping me with arguments

print('Termithon')
idkdwij = '''
    I   D       K   K   D       W         W     I       J
    I   D   D   K K     D  D    W    W    W     I   J   J
    I   D       K   K   D       W  W   W  W     I     J J
'''
print('The Python based terminal by' + idkdwij + 'it says idkdwij')
print('The source is here github.com/IDkDwij/termithon')

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


current_dir = os.getcwd()

commands = '''ls (shows files in current directory)
exit (exits program)
ip (gives you your ip)
hostname (gives you your computers id)
user (gives the user your logged on)
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
    elif cmd == 'ip':
        print(ip)
        main()
    elif cmd == 'hostname':
        print(hostname)
        main()
    elif cmd == 'user':
        print(getpass.getuser())
        main()
    else:
        print('invalid')
        main()


def main():
    global cmd
    cmd = input(current_dir + '>')
    whatiscommand()


lsdir = current_dir
main()
