import getpass
import platform
import os
import random
import socket
from uuid import getnode as get_mac
import time
import signal
import subprocess

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
os.system('cls||clear')
termithon = '''

 _______ _______  ______ _______ _____ _______ _     _  _____  __   _
    |    |______ |_____/ |  |  |   |      |    |_____| |     | | \  |
    |    |______ |    \_ |  |  | __|__    |    |     | |_____| |  \_|
                                                                      
                                                                                                                               
                                                                                                                               

'''
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

rohanisaidiot = '''                                        
         /             o          o    /o    _/_
 _   __ /_  __,  _ _  ,  (   __, ,  __/,  __ /  
/ (_(_)/ /_(_/(_/ / /_(_/_)_(_/(_(_(_/_(_(_)(__ 
'''
print(Fore.RED + termithon + Fore.WHITE)
print('The Python based terminal by' + Fore.LIGHTYELLOW_EX + idkdwij + Fore.WHITE + 'it says idkdwij')
print("IRL Friend/2nd developer" + Fore.GREEN + bigboytaco + Fore.WHITE)
print(Fore.MAGENTA + rohanisaidiot + Fore.WHITE)
print('The source is here github.com/IDkDwij/termithon')

# Setup
global current_dir
global echo_on
echo_on = False
PY_warning_said = False

# Get hostname
hostname = socket.gethostname()

# Get user's IP address
ip = socket.gethostbyname(hostname)

current_dir = os.getcwd()

commands = '''ls (shows files in current directory)
exit (exits program)
ip (gives you your ip)
hostname (gives you your computers id)
user (gives the user your logged on)
mac (gives you your mac addresss)
ping (lets you ping a website)
winfetch (A lot of info about your computer)
wifi ( gives you your wifi info and passwords)
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
# Function to print the interface


def handle_command(cmd, current_dir):
    global PY_warning_said
    args = cmd.split()
    
    if not args:
        return current_dir
    
    command = args[0]
    
    if command == 'help':
        print(commands)
    elif command == 'winfetch':
        os.system("powershell -File \"" + os.path.dirname(__file__) +"/winfetch.ps1\"")
    elif command == 'ls':
        print(os.listdir(current_dir))
    elif command == 'curl':
        os.system(cmd)
    elif command == "start":
        os.system(cmd)
    elif command == "cd":
        if len(args) < 2:
            print('The system cannot find the path specified.')
        else:
            path = ' '.join(args[1:])
            if os.path.isdir(path):
                current_dir = path
            elif os.path.isdir(os.path.join(current_dir, path)):
                current_dir = os.path.join(current_dir, path)
            else:
                print('The system cannot find the path specified.')
    elif command == 'exit':
        exit()
    elif command == 'ip':
        print(ip)
    elif command == 'hostname':
        print(hostname)
    elif command == 'user':
        print(getpass.getuser())
    elif command == "mac":
        print(mac)
    elif command == 'ping':
        os.system(cmd)
    elif command == "clear":
        os.system('cls||clear') 
    elif command == "mkdir":
        if len(args) < 2:
            print('Usage: mkdir <directory_name>')
        else:
            try:
                os.makedirs(args[1])
            except:
                os.makedirs(current_dir + args[1])
    elif command == "del":
        if len(args) < 2:
            print('Usage: del <file_name>')
        else:
            try:
                os.remove(args[1])
            except:
                os.remove(current_dir + args[1])
    elif command == 'echo':
        print(' '.join(args[1:]))
    elif command == 'python3':
        if not PY_warning_said:
            print('warning, this requires python3 to be installed')
            PY_warning_said = True
        os.system(cmd)
    elif command == 'pip':
        print('warning python must be installed to use this command')
        time.sleep(1)
        os.system(cmd)
    elif "color" in cmd:
        change_color(args)  
    elif "blackjack" in cmd:
        blackjack()
    elif command == "wifi":
        if platform.system() == "Windows":
            get_wifi_password_windows()
        else:
            print("Unsupported platform")
    else:
        Miscellaneous.commands(cmd, current_dir)

    return current_dir
def blackjack():
      print("placeholder")

def get_wifi_password_windows():
    output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [line.split(":")[1][1:-1] for line in output if "All User Profile" in line]
    for profile in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
            password = os.system('netsh wlan show profile name=' + profile + ' key=clear | find "Key Content"')
            if password:
                print(f"Wi-Fi Network: {profile}")
                print(f"Password: {password[0]}")
            else: 
                print(f"Wi-Fi Network: {profile}")
                print("Password not available for this network.")
        except Exception as e:
            print(f"Error occurred while retrieving password for {profile}: {str(e)}")


def change_color(args):
    if len(args) == 1 or args[1] == "help":
        print('''Available colors:
        0 = Black       8 = Gray
        1 = Blue        9 = Light Blue
        2 = Green       A = Light Green
        3 = Aqua        B = Light Aqua
        4 = Red         C = Light Red
        5 = Purple      D = Light Purple
        6 = Yellow      E = Light Yellow
        7 = White       F = Bright White''')
    elif args[1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']:
        print(Fore.RESET + f"Color changed to {args[1]}")
        if args[1] == '0':
            print(Fore.BLACK, end="")
        elif args[1] == '1':
            print(Fore.BLUE, end="")
        elif args[1] == '2':
            print(Fore.GREEN, end="")
        elif args[1] == '3':
            print(Fore.CYAN, end="")
        elif args[1] == '4':
            print(Fore.RED, end="")
        elif args[1] == '5':
            print(Fore.MAGENTA, end="")
        elif args[1] == '6':
            print(Fore.YELLOW, end="")
        elif args[1] == '7':
            print(Fore.WHITE, end="")
        elif args[1] == '8':
            print(Fore.LIGHTBLACK_EX, end="")
        elif args[1] == '9':
            print(Fore.LIGHTBLUE_EX, end="")
        elif args[1] == 'A':
            print(Fore.LIGHTGREEN_EX, end="")
        elif args[1] == 'B':
            print(Fore.LIGHTCYAN_EX, end="")
        elif args[1] == 'C':
            print(Fore.LIGHTRED_EX, end="")
        elif args[1] == 'D':
            print(Fore.LIGHTMAGENTA_EX, end="")
        elif args[1] == 'E':
            print(Fore.LIGHTYELLOW_EX, end="")
        elif args[1] == 'F':
            print(Fore.WHITE, end="")
    else:
        print("Invalid color code")


class Miscellaneous():
    @staticmethod
    def commands(cmd, current_dir):
        args = cmd.split()
        if args[0] == 'inspace':
            Miscellaneous.emulation()
        else:
            Miscellaneous.error(cmd)

    @staticmethod
    def emulation():
        chance = random.randint(1, 100)
        if chance > 2:
            print("You Died")
        else:
            print('You survived')

    @staticmethod
    def error(cmd):
        print("'" + str(cmd) + "'" + ''' is not recognized as an internal or external command (external commands not supported atm)''')

def main():
    global current_dir
    while True:
        cmd = input(f"{os.getlogin()}@{hostname}:{current_dir}$ ")
        current_dir = handle_command(cmd, current_dir)

if __name__ == "__main__":
    main()
