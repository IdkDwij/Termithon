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
 _______        _______                                       _     ____  ____        __           
|_   __ \      |_   __ \                                     / |_  |_   ||   _|      [  |          
  | |__) |_   __ | |__) |_ .--.   .--.   _ .--..--.  _ .--. `| |-'   | |__| |  .---.  | | _ .--.   
  |  ___/[ \ [  ]|  ___/[ `/'`\]/ .'`\ \[ `.-. .-. |[ '/'`\ \| |     |  __  | / /__\\ | |[ '/'`\ \ 
 _| |_    \ '/ /_| |_    | |    | \__. | | | | | | | | \__/ || |,   _| |  | |_| \__., | | | \__/ | 
|_____| [\_:  /|_____|  [___]    '.__.' [___||__||__]| ;.__/ \__/  |____||____|'.__.'[___]| ;.__/  
         \__.'                                      [__|                                 [__|      
1. dir (Shows files in current directory)
2. exit (Exits the terminal)
3. ip (Gives you your IP)
4. hostname (Gives you your Computer's ID)
5. mac (Retrieves the Physical MAC Address of The Device)
6. ping (lets you ping a website UPDATE: NOW ADDED!) 
7. calc (A simple calculator)
8. passgen (A very efficient password generator)
9. sysinfo (Gets relevant system info)
10. test (Tests PyPrompt Sample Command)
11. mp3search (Searches your File System for mp3 files)
12. mp4search (Searches your File System for mp4 files)
14. pysearch (Searches your File System for py files)
15. docxsearch (Searches your File System for docx files)
16. mailgen (Generates dummy E-Mail Addresses)
17. ver (Reports PyPrompt Version)
18. sudo (This uses the REAL sudo mode.) ONLY WORKS ON LINUX OR WSL
19. clear (Clears screen)
20. mkdir (Creates a folder)
21. del (deletes a file or directory) ONLY WORKS ON WINDOWS
22. rm (deletes a file or directory) ONLY WORKS ON LINUX OR MACOS
23. loadbarTest (Tests the loadbar)
24. diskpart (Opens up the real diskpart) ONLY WORKS ON WINDOWS
25. format (Formats a drive) ONLY WORKS ON WINDOWS
26. history (Shows all your command history) ONLY WORKS ON LINUX OR MACOS
27. hash (Displays program locations) ONLY WORKS ON LINUX OR MACOS
28. color (Changes the color of text) ONLY WORKS ON WINDOWS
29. intro (Displays initial text)
30. py (Opens up the Python shell, REQUIRES PYTHON TO BE INSTALLED!) ONLY WORKS ON WINDOWS
31. python (Alternate solution to the 'py' command) ONLY WORKS ON WINDOWS
32. python3 (Opens the Python shell, REQUIRES PYTHON 3 TO BE INSTALLED!) ONLY WORKS ON LINUX
33. pip (Opens up pip) REQUIRES PYTHON AND PIP TO BE INSTALLED!
34. wsl (Opens up the Linux shell, REQUIRES THE WINDOWS SUBSYSTEM FOR LINUX) ONLY WORKS ON WINDOWS!
35. apt (Command used to install package dependencies) ONLY WORKS ON LINUX
36. git (Opens up git, REQUIRES GIT TO BE INSTALLED!)
37. bash (Launches the bash terminal) ONLY WORKS ON LINUX OR WINDOWS (with wsl)
38. csh (Launches the C shell; REQUIRES csh to be installed) ONLY WORKS ON LINUX OR THE WSL
39. zsh (Launches the Z shell; REQUIRES zsh to be installed) ONLY WORKS ON LINUX OR THE WSL
40. unrar (Extracts files from a .rar file; REQUIRES unrar binary to be installed) ONLY WORKS ON LINUX
41. su (Enable or disable the sudo command) ONLY WORKS ON LINUX OR WSL
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
    import re, uuid
    print ("The MAC address of this Device is : ", end="")
    print (':'.join(re.findall('..', '%012x' % uuid.getnode())))
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
    def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='>'):
        percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}',end='\r')
        if iteration == total:
            print()
    items = list(range(0, 50))
    l = len(items)
    
    loadbar(0, l, prefix='Progress', suffix='Complete', length=l)
    for i, item in enumerate(items):
        sleep(0.1)
        loadbar(i + 1, l, prefix='Progress', suffix='Complete', length=l)

def intro():
    print("=" * 40, "PyPrompt", "=" * 40)
    print('Made by:' + joalricha + 'it says joalricha https://github.com/joalricha869')
    print(" ")
    print('Thanks to ' + taco + 'for help  https://github.com/BigBoyTaco')
    print(" ")
    print('Based on Termithron by' + dwij + 'https://github.com/IdkDwij/Termithron')
    print(" ")
    print('The source is here')
    print("Type in 'help' for the command list.")
    print("")

y = "1.2.1"


main()
