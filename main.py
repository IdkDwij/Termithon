#imports
from __future__ import division
import os
import string
import random
import socket
from random import choice
from random import randint
import platform
import fnmatch
import webbrowser
from time import sleep
import cmath
print("="*40, "PyPrompt", "="*40)
joalricha = '''
    _             _      _      _            ___    __ ___  
   (_)           | |    (_)    | |          / _ \  / // _ \ 
    _  ___   __ _| |_ __ _  ___| |__   __ _| (_) |/ /| (_) |
   | |/ _ \ / _` | | '__| |/ __| '_ \ / _` |> _ <| '_ \__, |
   | | (_) | (_| | | |  | | (__| | | | (_| | (_) | (_) |/ / 
   | |\___/ \__,_|_|_|  |_|\___|_| |_|\__,_|\___/ \___//_/  
  _/ |                                                      
 |__/                                                       

'''
taco = '''

  ____  _       ____           _______              
 |  _ \(_)     |  _ \         |__   __|             
 | |_) |_  __ _| |_) | ___  _   _| | __ _  ___ ___  
 |  _ <| |/ _` |  _ < / _ \| | | | |/ _` |/ __/ _ \ 
 | |_) | | (_| | |_) | (_) | |_| | | (_| | (_| (_) |
 |____/|_|\__, |____/ \___/ \__, |_|\__,_|\___\___/ 
           __/ |             __/ |                  
          |___/             |___/                   

'''
dwij = '''

  _     _ _    _____           _ _ 
 (_)   | | |  |  __ \         (_|_)
  _  __| | | _| |  | |_      ___ _ 
 | |/ _` | |/ / |  | \ \ /\ / / | |
 | | (_| |   <| |__| |\ V  V /| | |
 |_|\__,_|_|\_\_____/  \_/\_/ |_| |
                               _/ |
                              |__/ 

'''
print('Made by:' + joalricha + 'it says joalricha https://github.com/joalricha869')
print(" ")
print('Thanks to ' + taco + 'for help  https://github.com/BigBoyTaco')
print(" ")
print('Based on Termithron by' + dwij + 'https://github.com/IdkDwij/Termithron')
print(" ")
print('The source is here')
print("Type in 'help' for the command list.")
print("")
hostname = socket.gethostname()
current_dir = os.getcwd()
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1
commands = '''
  _____       _                       _           _ 
 |_   _|     | |                     | |         | |
   | |  _ __ | |_ ___  __ _ _ __ __ _| |_ ___  __| |
   | | | '_ \| __/ _ \/ _` | '__/ _` | __/ _ \/ _` |
  _| |_| | | | ||  __/ (_| | | | (_| | ||  __/ (_| |
 |_____|_| |_|\__\___|\__, |_|  \__,_|\__\___|\__,_|
                       __/ |                        
                      |___/                         

1. ip (Gives you your IP)
2. hostname (Gives you your Computer's ID)
3. mac (Retrieves the Physical MAC Address of The Device)
4. ping (lets you ping a website UPDATE: NOW ADDED!) not
5. calc (A simple calculator)
6. passgen (A very efficient password generator)
7. sysinfo (Gets relevant system info)
8. test (Tests PyPrompt Sample Command)
9. mp3search (Searches your File System for mp3 files)
10. mp4search (Searches your File System for mp4 files)
11. pysearch (Searches your File System for py files)
12. docxsearch (Searches your File System for docx files)
13. mailgen (Generates dummy E-Mail Addresses)
14. ver (Reports PyPrompt Version)
15. clear (Clears screen)
16. loadbarTest (Tests the loadbar)
17. intro (Displays initial text)
18. sqrt (Enter a number and it will calculate the square root)
19. date (Displays date)


   \  |        |  |   _)       |         |     _|               
  |\/ |  |  |  |   _|  |  _ \  |   _` |   _|   _| _ \   _| ` \  
 _|  _| \_,_| _| \__| _| .__/ _| \__,_| \__| _| \___/ _| _|_|_| 
                        _|                                      

1. git (Opens up git, REQUIRES GIT TO BE INSTALLED!)
2. pip (Opens up pip) REQUIRES PYTHON AND PIP TO BE INSTALLED!
3. dir (Shows files in current directory)
4. exit (Exits the terminal)
5. mkdir (Creates a folder)


  _      _                    _    _      _       
 | |    (_)                  | |  | |    | |      
 | |     _ _ __  _   ___  __ | |__| | ___| |_ __  
 | |    | | '_ \| | | \ \/ / |  __  |/ _ \ | '_ \ 
 | |____| | | | | |_| |>  <  | |  | |  __/ | |_) |
 |______|_|_| |_|\__,_/_/\_\ |_|  |_|\___|_| .__/ 
                                           | |    
                                           |_|    
                                           
1. sudo (This uses the REAL sudo mode.) ONLY WORKS ON LINUX OR WSL
2. rm (deletes a file or directory) ONLY WORKS ON LINUX OR WSL
3. history (Shows all your command history) ONLY WORKS ON LINUX OR WSL
4. hash (Displays program locations) ONLY WORKS ON LINUX OR WSL
5. python3 (Opens the Python shell, REQUIRES PYTHON 3 TO BE INSTALLED!) ONLY WORKS ON LINUX OR WSL
6. apt (Command used to install package dependencies) ONLY WORKS ON LINUX OR WSL
7. bash (Launches the bash terminal) ONLY WORKS ON LINUX OR WINDOWS (with wsl)
8. csh (Launches the C shell; REQUIRES csh to be installed) ONLY WORKS ON LINUX OR WSL
9. zsh (Launches the Z shell; REQUIRES zsh to be installed) ONLY WORKS ON LINUX OR WSL
10. unrar (Extracts files from a .rar file; REQUIRES unrar binary to be installed) ONLY WORKS ON LINUX OR WSL
11. su (Enable or disable the sudo command) ONLY WORKS ON LINUX OR WSL
12. cat (Creates a blank file) ONLY WORKS ON LINUX OR WSL

 __          ___           _                     _    _      _       
 \ \        / (_)         | |                   | |  | |    | |      
  \ \  /\  / / _ _ __   __| | _____      _____  | |__| | ___| |_ __  
   \ \/  \/ / | | '_ \ / _` |/ _ \ \ /\ / / __| |  __  |/ _ \ | '_ \ 
    \  /\  /  | | | | | (_| | (_) \ V  V /\__ \ | |  | |  __/ | |_) |
     \/  \/   |_|_| |_|\__,_|\___/ \_/\_/ |___/ |_|  |_|\___|_| .__/ 
                                                              | |    
                                                              |_|    


1. del (deletes a file or directory) ONLY WORKS ON WINDOWS
2. diskpart (Opens up the real diskpart) ONLY WORKS ON WINDOWS
3. format (Formats a drive) ONLY WORKS ON WINDOWS
4. color (Changes the color of text) ONLY WORKS ON WINDOWS
5. py (Opens up the Python shell, REQUIRES PYTHON TO BE INSTALLED!) ONLY WORKS ON WINDOWS
6. python (Alternate solution to the 'py' command) ONLY WORKS ON WINDOWS
7. wsl (Opens up the Linux shell, REQUIRES THE WINDOWS SUBSYSTEM FOR LINUX) ONLY WORKS ON WINDOWS!
8. cmd (Opens the Command Prompt) ONLY WORKS ON WINDOWS
9. ipconfig (Gives info about your IPV4 or IPV6 address, ip address, mac address) ONLY WORKS ON WINDOWS!

                        ____   _____   _    _      _       
                       / __ \ / ____| | |  | |    | |      
  _ __ ___   __ _  ___| |  | | (___   | |__| | ___| |_ __  
 | '_ ` _ \ / _` |/ __| |  | |\___ \  |  __  |/ _ \ | '_ \ 
 | | | | | | (_| | (__| |__| |____) | | |  | |  __/ | |_) |
 |_| |_| |_|\__,_|\___|\____/|_____/  |_|  |_|\___|_| .__/ 
                                                    | |    
                                                    |_|    

1. brew (The homebrew command) ONLY WORKS ON MACOS
2. softwareupdate (Checks for either macOS updates or software updates) ONLY WORKS ON MACOS
3. airport (Manage Apple AirPort) MIGHT REQUIRE zsh...   REQUIRES MACOS
'''

def whatiscommand():
    if cmd == 'help':
        print(commands)
        main()
    elif cmd == 'dir':
        print(os.listdir(current_dir))
        main()
    elif cmd == 'exit':
        exit()
    elif cmd == 'ip':
        print("Your IP Address is " + getip())
        main()
    elif cmd == 'hostname':
        uname = platform.uname()
        print(hostname)
        main()
    elif cmd == "mac":
        getmac()
        main()
    elif cmd == "calc":
        calc()
    elif cmd == "passgen":
        passGen()
    elif cmd == "sysinfo":
        getSystemInfo()
        main()
    elif cmd == "ver":
        ver()
        main()
    elif cmd == "test":
        testFunc()
        main()
    elif cmd == "mp3search":
        mp3search()
        main()
    elif cmd == "mp4search":
        mp3search()
        main()
    elif cmd == "pysearch":
        pysearch()
        main()
    elif cmd == "docxsearch":
        docxsearch()
        main()
    elif cmd == "mailgen":
        mailGen()
        main()
    elif cmd == "clear":
        clear()
    elif "mkdir" in cmd:
        os.system(cmd)
        main()
    elif "rm" in cmd:
        os.system(cmd)
        main()
    elif "del" in cmd:
        os.system(cmd)
        main()
    elif "loadbarTest" in cmd:
        progressbar()
        main()
    elif "diskpart" in cmd:
        os.system(cmd)
        main()
    elif "format" in cmd:
        os.system(cmd)
        main()
    elif "history" in cmd:
        os.system(cmd)
        main()
    elif "hash" in cmd:
        os.system(cmd)
        main()
    elif "color" in cmd:
        os.system(cmd)
        main()
    elif "intro" in cmd:
        intro()
        main()
    elif "sudo bitcoinminer" in cmd:
        rootPerms()
        btcminer()
        main()
    elif "py" in cmd:
        os.system(cmd)
        main()
    elif "python3" in cmd:
        os.system(cmd)
        main()
    elif "python" in cmd:
        os.system(cmd)
        main()
    elif "pip" in cmd:
        os.system(cmd)
        main()
    elif "wsl" in cmd:
        os.system(cmd)
        main()
    elif "apt" in cmd:
        os.system(cmd)
        main()
    elif "git" in cmd:
        os.system(cmd)
        main()
    elif "ping" in cmd:
        os.system(cmd)
        main()
    elif "bash" in cmd:
        os.system(cmd)
        main()
    elif "csh" in cmd:
        os.system(cmd)
        main()
    elif "zsh" in cmd:
        os.system(cmd)
        main()
    elif "unrar" in cmd:
        os.system(cmd)
        main()
    elif "sudo" in cmd:
        os.system(cmd)
        main()
    elif "su" in cmd:
        os.system(cmd)
        main()
    elif "cmd" in cmd:
        os.system(cmd)
        main()
    elif "brew" in cmd:
        os.system(cmd)
        main()
    elif "softwareupdate" in cmd:
        os.system(cmd)
        main()
    elif "airport" in cmd:
        os.system(cmd)
        main()
    elif "ipconfig" in cmd:
        os.system(cmd)
        main()
    elif "cat" in cmd:
        os.system(cmd)
        main()
    elif "sqrt" in cmd:
        sqrt()
        main()
    elif "date" in cmd:
        date()
        main()
    else:
        error()
def main():
    global cmd
    cmd = input(current_dir + '>')
    whatiscommand()
def ver():
    print("PyPrompt Version: " + y)
    print("(C) 2022 joalricha869, All Rights Reserved.")
def getSystemInfo():
    print("="*40, "System Information", "="*40)
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")
    print("System Info Retrieved!")
def calc():
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        while True:
            choice = input("Enter choice(1/2/3/4): ")
            if choice in ('1', '2', '3', '4'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == '1':
                    print(num1, "+", num2, "=", add(num1, num2))
                elif choice == '2':
                    print(num1, "-", num2, "=", subtract(num1, num2))
                elif choice == '3':
                    print(num1, "*", num2, "=", multiply(num1, num2))
                elif choice == '4':
                    print(num1, "/", num2, "=", divide(num1, num2))
                next_calculation = input("Let's do next calculation? (yes/no): ")
                if next_calculation == "no":
                  main()
            else:
                print("Invalid Input")
                main()
def passGen():
        characters = string.ascii_letters + string.punctuation  + string.digits
        password =  "".join(choice(characters) for x in range(randint(8, 16)))
        print("Is your Generated Password: ",password)
        repeatGen = input("Generate another one? ")
        if repeatGen == "yes":
            passGen()
        else:
            main()
def getmac():
    import uuid
    print ("The MAC address of this Device is : ", end="")
    print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
    for ele in range(0,8*6,8)][::-1]))
def getip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:       
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP
def clear():
    os.system('cls||clear')
    main()
def error():
    if(cmd == ""):
        main()
    else:
        print("'" + str(cmd) + "'" + ''' is not recognized as an internal or external command''')
        print("For more help go to: https://github.com/joalricha869/PyPrompt or https://github.com/IdkDwij/Termithon")
        main()
def testFunc():
    print("If this command works, then your PyPrompt is fine... maybe")
def mp3search():
    rootPath = '/'
    pattern = '*.mp3'
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            print( os.path.join(root, filename))
def mp4search():
    rootPath = '/'
    pattern = '*.mp4'
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            print( os.path.join(root, filename))
def pysearch():
    rootPath = '/'
    pattern = '*.py'
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            print( os.path.join(root, filename))
def docxsearch():
    rootPath = '/'
    pattern = '*.docx'
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            print( os.path.join(root, filename))
def mailGen():
    extensions = ['com']
    domains = ['gmail','yahoo','comcast','verizon','charter','hotmail','outlook','frontier','icloud','yandex']
    characters = string.ascii_letters + string.digits
    winext = extensions[random.randint(0,len(extensions)-1)]
    windom = domains[random.randint(0,len(domains)-1)]
    acclen = random.randint(1,20)
    winacc = ''.join(choice(characters) for _ in range(acclen))
    finale = winacc + "@" + windom + "." + winext
    progressbar()
    print("Your Generated E-Mail Address is: ",finale)
    again = input("Generate another address? ")
    if again == "yes":
        progressbar()
        mailGen()
    else:
        main()
def progressbar():
    def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
        percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '▒' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}',end='\r')
        if iteration == total:
            print()
    items = list(range(0, 50))
    l = len(items)
    
    loadbar(0, l, prefix='Generating...', suffix='Done!', length=l)
    for i, item in enumerate(items):
        sleep(0.1)
        loadbar(i + 1, l, prefix='Generating...', suffix='Done!', length=l)

def intro():
    print("=" * 40, "PyPrompt", "=" * 40)
    print('Made by:' + joalricha + 'it says joalricha https://github.com/joalricha869')
    print(" ")
    print('Thanks to ' + taco + 'for help  https://github.com/BigBoyTaco')
    print(" ")
    print('Based on Termithron Shell by' + dwij + 'https://github.com/IdkDwij/Termithron')
    print(" ")
    print('The source is here')
    print("Type in 'help' for the command list.")
    print("")

def sqrt():
    num = float(input('Enter a number: '))
    num_sqrt = num ** 0.5
    print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))

def date():
    from datetime import date
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    print("Today's date is:", d2)
    main()

y = "1.2.2.1"


main()
