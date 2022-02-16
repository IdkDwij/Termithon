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

#setup
PY_warning_said = bool(False)
#get hostname
hostname = socket.gethostname()
#gets users ip addresss
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
python3 (full python3 support [only if you have python3 installed])
cd (change current working directory)
del (windows delete command)
mkdir (windows make folder command)
echo (echo something or create something)
clear (clear terminal)
For more help go to github.com/IDkDwij/termithon
'''



def main(current_dir):
    global cmd
    cmd = input(current_dir + '>')
    whatiscommand(current_dir)


def whatiscommand(current_dir):
    #help command
    if cmd == 'help':
        print(commands)
        main(current_dir)
    #ls command
    elif cmd == 'ls':
        print(os.listdir(current_dir))
        main(current_dir)
    #cd command
    elif "cd" in cmd:
        args = cmd.split()
        if os.path.isdir(args[1]) == True:
            current_dir = args[1]
            main(current_dir)
        else:
            print('The system cannot find the path specified. \n')
            main(current_dir)
    #exit command
    elif cmd == 'exit':
        exit()
    #ip command
    elif cmd == 'ip':
        print(ip)
        main(current_dir)
    #hostname command
    elif cmd == 'hostname':
        print(hostname)
        main(current_dir)
    #users command
    elif cmd == 'user':
        print(getpass.getuser())
        main(current_dir)
    #mac address command
    elif cmd == "mac":
        print(mac)
        main(current_dir)
    #ping command
    elif "ping" in cmd:
        os.system(cmd)
        main(current_dir)
     #clear command
    elif cmd == "clear":
        os.system('cls||clear')
        main(current_dir)
    elif "mkdir" in cmd:
        os.system(cmd)
        main(current_dir)
        
    elif "del" in cmd:
        os.system(cmd)
        main(current_dir)
        
    elif "echo" in cmd:
        os.system(cmd)
        main(current_dir)
        
    #python command
    elif 'python3' in cmd:
        global PY_warning_said
        if PY_warning_said == False:
            print('warning, this reqires python3 to be installed')
            PY_warning_said = True
            os.system(cmd)
            main(current_dir)
        else:
            os.system(cmd)
            main(current_dir)
    elif cmd == "":
        main(current_dir)
    else:
        Miscellaneous.commands(self=None)





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
        main(current_dir)
    def error(self):
        print("'" + str(cmd) + "'" + ''' is not recognized as an internal or external command (external commands not supported atm)''')
        main(current_dir)


main(current_dir)
