import getpass
import os
import random
import socket
from uuid import getnode as get_mac
import time
try:
    import colorama
    from colorama import Fore
except:
    print("Colorama package not found, installing Colorama")
    os.system("pip install colorama")
    print('Termithon restart required')
    print('closing in 5 seconds')
    time.sleep(5)
    exit()
mac = get_mac()
# Made in python
# collaborated with https://github.com/BigBoyTaco/ for this little update
# thanks for green1490#2863 for helping me with arguments
os.system('cls||clear')
print(Fore.RED + 'Termithon' + Fore.WHITE)
idkdwij = '''
    I   D       K   K   D       W         W     I       J
    I   D   D   K K     D  D    W    W    W     I   J   J
    I   D       K   K   D       W  W   W  W     I     J J
'''
bigboytaco = '''
  ____  _       ____           _______              
 |  _ \(_)     |  _ \         |__   __|             
 | |_) |_  __ _| |_) | ___  _   _| | __ _  ___ ___  
 |  _ <| |/ _` |  _ < / _ \| | | | |/ _` |/ __/ _ \ 
 | |_) | | (_| | |_) | (_) | |_| | | (_| | (_| (_) |
 |____/|_|\__, |____/ \___/ \__, |_|\__,_|\___\___/ 
           __/ |             __/ |                  
          |___/             |___/   '''
print('The Python based terminal by' + idkdwij + 'it says idkdwij')
print("IRL Friend/2nd devloper" + Fore.GREEN + bigboytaco + Fore.WHITE)
print('The source is here github.com/IDkDwij/termithon')
#setup
global current_dir
global echo_on
echo_on = False
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
pip (python pip command)
cd (change current working directory)
del (deletes file)
mkdir (creates folder)
echo (echo something or create something [not currently working])
clear (clear terminal)
curl (the curl command)
start (run something)
color (change text color)

For more help go to github.com/IDkDwij/termithon
'''

def main(current_dir):
    global old_dir
    old_dir = current_dir
    global cmd
    cmd = input(current_dir + '>')
    whatiscommand(current_dir)

def whatiscommand(current_dir):
    args = cmd.split()
    #help command
    if cmd == 'help':
        print(commands)
        main(current_dir)
    #ls command
    elif cmd == 'ls':
        print(os.listdir(current_dir))
        main(current_dir)
    elif 'curl' in cmd:
        os.system(cmd)
        main(current_dir)
    #start command
    elif "start" in cmd:
        os.system(cmd)
    #cd command
    elif "cd" in cmd:
        args.remove('cd')
        args = ' '.join(args)
        if cmd == "cd":
            main(current_dir)
        old_dir = current_dir
        if os.path.isdir(args) == True:
            current_dir = args
            main(args)
        elif os.path.isdir(old_dir + '\\' + args):
            new_dir = old_dir + '\\' + args
            current_dir = new_dir
            main(new_dir)
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
        try:
            os.makedirs(args[1])
        except:
            os.makedirs(current_dir + args[1])
        main(current_dir)
    elif "del" in cmd:
        try:
            os.remove(args[1])
        except:
            os.remove(current_dir + args[1])
        main(current_dir)
    elif 'echo' in cmd:
        args.remove('echo')
        args = ' '.join(args)
        print(args)
        main(current_dir)
    #python command
    elif 'python3' in cmd:
        global PY_warning_said
        if PY_warning_said == False:
            print(Fore.RED + 'warning, this reqires python3 to be installed' + Fore.WHITE)
            PY_warning_said = True
            os.system(cmd)
            main(current_dir)
        else:
            os.system(cmd)
            main(current_dir)
    elif cmd == "":
        main(current_dir)
    elif 'pip' in cmd:
        print(Fore.RED + 'warning python must be installed to use this commnad' + Fore.WHITE)
        time.sleep(1)
        os.system(cmd)
        main(current_dir)
    elif 'color' in cmd:
        #color help
        if(cmd == 'color'):
            print('''All colors:
        0 = Black       8 = Light Blue
        1 = Blue        9 = Light Green
        2 = Green       A = Light Aqua
        3 = Aqua        B = Light Red
        4 = Red         C = Light Purple
        5 = Purple      D = Light Yellow
        6 = Yellow      7 = White''')
        elif(cmd == 'color 0'):
            print(Fore.BLACK)
        elif(cmd == 'color 1'):
            print(Fore.BLUE)
        elif(cmd == 'color 2'):
            print(Fore.GREEN)
        elif(cmd == 'color 3'):
            print(Fore.CYAN)
        elif(cmd == 'color 4'):
            print(Fore.RED)
        elif(cmd == "color 5"):
            print(Fore.MAGENTA)
        elif(cmd == 'color 6'):
            print(Fore.YELLOW)
        elif(cmd == 'color 7'):
            print(Fore.WHITE)
        elif(cmd == 'color 8'):
            print(Fore.LIGHTBLUE_EX)
        elif(cmd == 'color 9'):
            print(Fore.LIGHTGREEN_EX)
        elif(cmd == 'color a'):
            print(Fore.LIGHTCYAN_EX)
        elif(cmd == 'color b'):
            print(Fore.LIGHTRED_EX)
        elif(cmd == 'color c'):
            print(Fore.LIGHTMAGENTA_EX)
        elif(cmd == 'color d'):
            print(Fore.LIGHTYELLOW_EX)
        else:
            print('color not recognized use "color" for help')
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
