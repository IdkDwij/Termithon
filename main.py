import getpass
import os
import random
import socket
from uuid import getnode as get_mac

mac = get_mac()
# Made in python
# collaborated with https://github.com/BigBoyTaco/ for this little update
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
mac (gives you your mac addresss)
ping (lets you ping a website)
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
    #help command
    if cmd == 'help':
        print(commands)
        main()
    #ls command
    elif cmd == 'ls':
        print(os.listdir(current_dir))
        main()
    #cd command
    elif cmd == "cd":
        global args
        args = cmd
        cdCmd()
    #exit command
    elif cmd == 'exit':
        exit()
    #ip command
    elif cmd == 'ip':
        print(ip)
        main()
    #hostname command
    elif cmd == 'hostname':
        print(hostname)
        main()
    #users command
    elif cmd == 'user':
        print(getpass.getuser())
        main()
    #mac address command
    elif cmd == "mac":
        print(mac)
        main()
    elif "ping" in cmd:
        os.system(cmd)
    elif cmd == "":
        main()
    else:
        Miscellaneous.commands(self=None)


def main():
    global cmd
    cmd = input(current_dir + '>')
    whatiscommand()



class Miscellaneous():
    def commands(self):
        if cmd == 'inspace':
            Miscellaneous.emulation(self=None)
        else:
            Miscellaneous.error(self=None)
    def emulation(self):
        chance = random.randint(1,100)
        if chance > 2:
            print("You Died")
        else:
            print('You survived')
        main()
    def error(self):
        print("'" + str(cmd) + "'" + ''' is not recognized as an internal or external command''')
        main()


main()
