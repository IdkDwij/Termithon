import getpass
import os
import platform
import random
import socket
import subprocess
import time
from datetime import timedelta
from uuid import getnode as get_mac
try:
    import psutil
    import shutil
    from win32api import GetSystemMetrics
    import GPUtil
    from colorama import Fore, Style

except:
    print("Required package not found, installing")
    os.system("pip install colorama")
    os.system("pip install pywin32")
    os.system("pip install shutils")
    os.system("pip install gpuinfo")
    os.system("pip install psutil")
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

commands = f'''
{Fore.CYAN}1. {Fore.WHITE}ls (shows files in current directory)
{Fore.CYAN}2. {Fore.WHITE}exit (exits program)
{Fore.CYAN}3. {Fore.WHITE}ip (gives you your ip)
{Fore.CYAN}4. {Fore.WHITE}hostname (gives you your computer's id)
{Fore.CYAN}5. {Fore.WHITE}user (gives the user you're logged on)
{Fore.CYAN}6. {Fore.WHITE}mac (gives you your mac address)
{Fore.CYAN}7. {Fore.WHITE}ping (lets you ping a website)
{Fore.CYAN}8. {Fore.WHITE}diafetch (A lot of info about your computer)
{Fore.CYAN}9. {Fore.WHITE}python3 (full python3 support [only if you have python3 installed])
{Fore.CYAN}10. {Fore.WHITE}pip (python pip command)
{Fore.CYAN}11. {Fore.WHITE}cd (change current working directory)
{Fore.CYAN}12. {Fore.WHITE}del (deletes file)
{Fore.CYAN}13. {Fore.WHITE}mkdir (creates folder)
{Fore.CYAN}14. {Fore.WHITE}echo (echo something or create something [not currently working])
{Fore.CYAN}15. {Fore.WHITE}clear (clear terminal)
{Fore.CYAN}16. {Fore.WHITE}curl (the curl command)
{Fore.CYAN}17. {Fore.WHITE}start (run something)
{Fore.CYAN}18. {Fore.WHITE}color (change text color)
{Fore.CYAN}19. {Fore.WHITE}packagelist (All installed python packages)

For more help go to github.com/IDkDwij/termithon
'''


def handle_command(cmd, current_dir):
    global PY_warning_said
    args = cmd.split()
    
    if not args:
        return current_dir
    
    command = args[0]
    
    if command == 'help':
        print(commands)
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
        print(Fore.CYAN + ip + Fore.WHITE)
    elif command == 'hostname':
        print(Fore.CYAN + hostname + Fore.WHITE)
    elif command == 'user':
        print(Fore.CYAN + getpass.getuser() + Fore.WHITE)
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
        print(Fore.CYAN + ' '.join(args[1:]) + Fore.WHITE)
    elif command == 'python3':
        if not PY_warning_said:
            print(Fore.CYAN + 'warning, this requires python3 to be installed' + Fore.WHITE)
            PY_warning_said = True
        os.system(cmd)
    elif command == 'pip':
        print(Fore.CYAN + 'warning python must be installed to use this command' + Fore.WHITE)
        time.sleep(1)
        os.system(cmd)
    elif "color" in cmd:
        change_color(args)  
    elif command == "wifi":
        if platform.system() == "Windows":
            get_wifi_password_windows()
        else:
            print(Fore.CYAN + "Unsupported platform" + Fore.WHITE)
    elif command == "casino":
        casino()
    elif command == "diafetch":
        diafetch()
    elif command == "packagelist":
        diafetch_package_list()
    else:
        Miscellaneous.commands(cmd, current_dir)

    return current_dir

def get_installed_packages_count():
    installed_packages_count = len(list(pkg_resources.working_set))
    return installed_packages_count

def diafetch():
    try:
        gpu_name = GPUtil.getGPUs()[0].name
    
      
        installed_packages_count = get_installed_packages_count()

    
        uname = platform.uname()
        system = uname.system
        hostname = socket.gethostname()
        uptime_seconds = time.time() - psutil.boot_time()
        uptime_string = str(timedelta(seconds=uptime_seconds))
        cpu_info = f"{psutil.cpu_percent()}% {psutil.cpu_freq().max:.2f}MHz {psutil.cpu_count(logical=False)} cores"
        memory_info = psutil.virtual_memory()
        total_memory = memory_info.total / (1024**3)  # Convert bytes to GB
        used_memory = memory_info.used / (1024**3)
        total, used, free = shutil.disk_usage("/")
        total_disk = total / (1024**3)
        used_disk = used / (1024**3)
        resolution = "N/A"

        if platform.system() == "Windows":
            from win32api import GetSystemMetrics
            resolution = f"{GetSystemMetrics(0)}x{GetSystemMetrics(1)}"


        print(Fore.CYAN + "        ___                ")
        print(Fore.CYAN + "      /    /\              User: " + Fore.WHITE + f"{getpass.getuser()}")
        print(Fore.CYAN + "     /    /  \             Host: " + Fore.WHITE + f"{hostname}")
        print(Fore.CYAN + "    /    /    \            OS: " + Fore.WHITE + f"{system}")
        print(Fore.CYAN + "   /    /  /\  \           Kernel: " + Fore.WHITE + f"{uname.release}")
        print(Fore.CYAN + "  /    /  /  \  \          Uptime: " + Fore.WHITE + f"{uptime_string}")
        print(Fore.CYAN + " /    /  /    \  \         Packages: " + Fore.WHITE + f"{installed_packages_count}")
        print(Fore.CYAN + "/____/  /      \  \        Shell: " + Fore.WHITE + "Python")
        print(Fore.CYAN + "\    \  \      /  /        Resolution: " + Fore.WHITE + f"{resolution}")
        print(Fore.CYAN + " \    \  \    /  /         Terminal: " + Fore.WHITE + "Termithon")
        print(Fore.CYAN + "  \    \  \  /  /          CPU: " + Fore.WHITE + f"{cpu_info}")
        print(Fore.CYAN + "   \    \  \/  /           GPU: " + Fore.WHITE + f"{gpu_name}")
        print(Fore.CYAN + "    \    \    /            Memory: " + Fore.WHITE + f"{used_memory:.2f}GB / {total_memory:.2f}GB")
        print(Fore.CYAN + "     \    \  /             Disk: " + Fore.WHITE + f"{used_disk:.2f}GB / {total_disk:.2f}GB")
        print(Fore.CYAN + "      \____\/              ")
        print(Style.RESET_ALL)
    
    except Exception as e:
        print(Fore.RED + f"An error occurred in diafetch: {str(e)}" + Fore.WHITE)

def get_installed_packages():
    installed_packages = []
    for package in pkg_resources.working_set:
        installed_packages.append(package.key)
    return installed_packages

def diafetch_package_list():
    try:
        installed_packages = get_installed_packages()
        num_packages = len(installed_packages)
        print(Fore.CYAN + "Installed Packages:")
        for i, package in enumerate(installed_packages):
            if (i + 1) % 3 == 0:  
                end = '\n'
            else:
                end = ' ' + Style.RESET_ALL + ' '
            print(f"{Fore.CYAN}{i + 1}. {Fore.WHITE}{package.ljust(20)}", end=end)
        print()  
    except Exception as e:
        print(Fore.RED + f"An error occurred in diafetch pl: {str(e)}")

def casino():
    print(Fore.GREEN + '''

    1. Blackjack
    2. Roulette
    3. Poker
    4. Slots
    
    Q to Quit
            
''' + Fore.WHITE)
    
    choice = input("Which game would you like to play: ")

    if choice == '1':
        blackjack()
    elif choice == '2':
        roulette()
    elif choice == '3':
        poker()
    elif choice == '4':
        slots()
    elif choice.lower() == 'q':
        main()
    else:
        print("\n" + Fore.RED + "Bad Input Try Again" + Fore.WHITE)
        casino()
    
def blackjack():
    print("Placeholder")

def roulette():
    print("Placeholder")

def poker():
    print("Placeholder")

def slots():
    print("Placeholder")



def get_wifi_password_windows():
    output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [line.split(":")[1][1:-1] for line in output if "All User Profile" in line]
    for profile in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
            password_line = [line for line in results if "Key Content" in line]
            if password_line:
                password = password_line[0].split(":")[1].strip()
                print(Fore.CYAN + "_" * 40 + Fore.WHITE)
                print(f"\nNetwork: {profile}")
                print(f"\nPassword: {password}")
            else:
                print(f"\nNetwork: {profile}")
                print("\nPassword not available for this network.")
    
            print(Fore.CYAN + "_" * 40 + Fore.WHITE)
            print(" " * 40)
            print(" " * 40)
        except Exception as e:
            print(f"\nError occurred while retrieving password for {profile}: {str(e)}")



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
