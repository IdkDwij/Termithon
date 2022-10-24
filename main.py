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
    if args[0] == 'help':
        print(commands)
        main(current_dir)
    #ls command
    elif args[0] == 'ls':
        print(os.listdir(current_dir))
        main(current_dir)
    elif args[0] == 'curl':
        os.system(cmd)
        main(current_dir)
    #start command
    elif args[0] == "start":
        os.system(cmd)
    #cd command
    elif args[0] == "cd":
        args.remove('cd')
        args = ' '.join(args)
        if args[0] == "cd":
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
    elif args[0] == 'exit':
        exit()
    #ip command
    elif args[0] == 'ip':
        print(ip)
        main(current_dir)
    #hostname command
    elif args[0] == 'hostname':
        print(hostname)
        main(current_dir)
    #users command
    elif args[0] == 'user':
        print(curr_user())
        main(current_dir)
    #mac address command
    elif args[0] == "mac":
        print(mac)
        main(current_dir)
    #ping command
    elif args[0] == 'ping':
        os.system(cmd)
        main(current_dir)
     #clear command
    elif args[0] == "clear":
        os.system('cls||clear')
        main(current_dir)
    elif args[0] == "mkdir":
        try:
            os.makedirs(args[1])
        except:
            os.makedirs(current_dir + args[1])
        main(current_dir)
    elif args[0] == "del":
        try:
            os.remove(args[1])
        except:
            os.remove(current_dir + args[1])
        main(current_dir)
    elif args[0] == 'echo':
        args.remove('echo')
        args = ' '.join(args)
        print(args)
        main(current_dir)
        
    #python command
    elif args[0] == 'python3':
        global PY_warning_said
        if PY_warning_said == False:
            print('warning, this reqires python3 to be installed')
            PY_warning_said = True
            os.system(cmd)
            main(current_dir)
        else:
            os.system(cmd)
            main(current_dir)
    elif args[0] == "":
        main(current_dir)
    elif  "color" in cmd:
        color(current_dir,cur_color)
    elif args[0] == 'pip':
        print('warning python must be installed to use this commnad')
        time.sleep(1)
        os.system(cmd)
        main(current_dir)
    else:
        Miscellaneous.commands(current_dir,cur_color)
class Miscellaneous():
    def commands(current_dir,cur_color):
        if args[0] == 'inspace':
            Miscellaneous.emulation(current_dir,cur_color)
        else:
            Miscellaneous.error(current_dir,cur_color)
    def emulation(current_dir,cur_color):
        chance = random.randint(1,100)
        if chance > 2:
            print("You Died")
        else:
            print('You survived')
        main(current_dir)
    def error(current_dir):
        print("'" + str(cmd) + "'" + ''' is not recognized as an internal or external command (external commands not supported atm)''')
        main(current_dir)

def color(current_dir):
    args = cmd.split()
    if args[0] == "color":
        print('''       0 = Black       8 = Gray
        1 = Blue        9 = Light Blue
        2 = Green       A = Light Green
        3 = Aqua        B = Light Aqua
        4 = Red         C = Light Red
        5 = Purple      D = Light Purple
        6 = Yellow      E = Light Yellow
        7 = White       F = Bright White''')
    elif args[1] == "help":
        print('''            0 = Black       8 = Gray
            1 = Blue        9 = Light Blue
            2 = Green       A = Light Green
            3 = Aqua        B = Light Aqua
            4 = Red         C = Light Red
            5 = Purple      D = Light Purple
            6 = Yellow      E = Light Yellow
            7 = White       F = Bright White''')
    elif args[1] == "1":
        cur_color = Fore.BLUE
    elif args[1] == "2":
        cur_color = Fore.GREEN
    elif args[1] == "3":
        cur_color = Fore.CYAN
    elif args[1] == "4":
        cur_color = Fore.RED
    elif args[1] == "5":
        cur_color = Fore.RED
    elif args[1] == "6":
        cur_color = Fore.YELLOW
    elif args[1] == "7":
        cur_color = Fore.WHITE
    elif args[1] == "8":
        cur_color = Fore.LIGHTBLACK_EX
    elif args[1] == "9":
        cur_color = Fore.LIGHTBLUE_EX
    elif args[1] == "0":
        cur_color = Fore.BLACK
    elif args[1].lower() == "a":
        cur_color = Fore.BLUE
    elif args[1].lower() == "c":
        cur_color = Fore.LIGHTRED_EX
    elif args[1].lower() == "d":
        cur_color = Fore.LIGHTMAGENTA_EX
    elif args[1].lower() == "e":
        cur_color = Fore.LIGHTYELLOW_EX
    elif args[1].lower() == "f":
        cur_color = Fore.LIGHTWHITE_EX
    main(current_dir)

main(current_dir)
