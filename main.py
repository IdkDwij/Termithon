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
import subprocess
import argparse
from ast import For, arg
import time
from time import sleep
try:
    import googletrans
    from googletrans import Translator
except:
    print("WARNING! Package Install Can't Operate Under Restricted Proxy...")
    print("Googletrans Package Not Found")
    print("Installing now...")
    os.system("pip install googletrans")
    print("If error thrown, update your Python or reinstall.")
    time.sleep(3)
    os.system('cls||clear')
    print("PyPrompt Closing in 5 Seconds")
    time.sleep(1)
    os.system('cls||clear')
    print("PyPrompt Closing in 4 Seconds")
    time.sleep(1)
    os.system('cls||clear')
    print("PyPrompt Closing in 3 Seconds")
    time.sleep(1)
    os.system('cls||clear')
    print("PyPrompt Closing in 2 Seconds")
    time.sleep(1)
    os.system('cls||clear')
    print("PyPrompt Closing in 1 Second")
    time.sleep(1)
    exit()

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
print("The source is at my GitHub page! 'https://github.com/joalricha869/PyPrompt'")
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
20. wifipassword (Gets your wifi password) (MIGHT NOT BE COMPATIBLE WITH Python 3.8 or earlier.)
21. translator (Usage: translator -s <source_lang> -d <destination_lang>) (MIGHT NOT BE COMAtiBLE WITH Python 3.8 or earlier.)
22. installer (DEBUG Command to check installation of 'translate' module)

The PyPrompt can be used as an alternative terminal shell. It can run every shell command from WIndows and UNIX

'''

def whatiscommand(current_dir):
    args = cmd.split()
    if cmd == 'help':
        print(commands)
        main(current_dir)
    elif cmd == 'dir':
        print(os.listdir(current_dir))
        main(current_dir)
    elif cmd == 'exit':
        exit()
    elif cmd == 'ip':
        print("Your IP Address is " + getip())
        main(current_dir)
    elif cmd == 'hostname':
        uname = platform.uname()
        print(hostname)
        main(current_dir)
    elif cmd == "mac":
        getmac()
        main(current_dir)
    elif cmd == "calc":
        calc()
    elif cmd == "passgen":
        passGen()
    elif cmd == "sysinfo":
        getSystemInfo()
        main(current_dir)
    elif cmd == "ver":
        ver()
        main(current_dir)
    elif cmd == "test":
        testFunc()
        main(current_dir)
    elif cmd == "mp3search":
        mp3search()
        main(current_dir)
    elif cmd == "mp4search":
        mp3search()
        main(current_dir)
    elif cmd == "pysearch":
        pysearch()
        main(current_dir)
    elif cmd == "docxsearch":
        docxsearch()
        main(current_dir)
    elif cmd == "mailgen":
        mailGen()
        main(current_dir)
    elif cmd == "clear":
        clear()
    elif "loadbarTest" in cmd:
        progressbar()
        main(current_dir)
    elif "intro" in cmd:
        intro()
        main(current_dir)
    elif "sqrt" in cmd:
        sqrt()
        main(current_dir)
    elif "date" in cmd:
        date()
        main(current_dir)
    elif "ignore" in cmd:
        easterEgg()
        main(current_dir)
    elif "wifipassword" in cmd:
        wifipassword()
        main(current_dir)
    elif "translator" in cmd:
        translate()
        main(current_dir)
    elif "installer" in cmd:
        installer()
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
    elif str(cmd) in cmd:
        print("This MUST be a shell command in the OS else your command won't work!")
        os.system(cmd)
        main(current_dir)
    else:
        error()
def main(current_dir):
    global old_dir
    old_dir = current_dir
    global cmd
    cmd = input(current_dir + '>')
    whatiscommand(current_dir)
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
                  main(current_dir)
            else:
                print("Invalid Input")
                main(current_dir)
def passGen():
        characters = string.ascii_letters + string.punctuation  + string.digits
        password =  "".join(choice(characters) for x in range(randint(8, 16)))
        print("Is your Generated Password: ",password)
        repeatGen = input("Generate another one? ")
        if repeatGen == "yes":
            passGen()
        else:
            main(current_dir)
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
    main(current_dir)
def error():
    if(cmd == ""):
        main(current_dir)
    else:
        print("'" + str(cmd) + "'" + ''' is not recognized as an internal or external command''')
        print("For more help go to: https://github.com/joalricha869/PyPrompt or https://github.com/IdkDwij/Termithon")
        main(current_dir)
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
        main(current_dir)
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
    main(current_dir)

def easterEgg():
    print("This terminal was made by Jose a.k.a joalricha869")
    print("Base code that this is powered by made by Dwij a.k.a idkDwij")
    print("Some help by Nathan a.k.a BigBoyTaco")
    print("This used to be Termithron 3.0 once.")

def wifipassword():
    systemInfo=''
    try:
        systemInfo = subprocess.check_output(['uname']).decode('utf-8', errors="backslashreplace").split('\n')
        systemInfo = systemInfo[0]
    except :
        pass
    if systemInfo == "Linux":
        wifiData = subprocess.check_output(['ls', '/etc/NetworkManager/system-connections']).decode('utf-8', errors="backslashreplace").split('\n')
        print ("Wifiname                       Password")
        print ("----------------------------------------")
    
        for wifiname in wifiData:
            if wifiname != '':
                wifiPass = subprocess.check_output(['sudo','cat', f"/etc/NetworkManager/system-connections/{wifiname}"]).decode('utf-8', errors="backslashreplace").split('\n')
                password=wifiPass[15].strip("psk=");
                print ("{:<30} {:<}".format(wifiname, password))
    else:
        wifi = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
        profiles = [i.split(":")[1][1:-1] for i in wifi if "All User Profile" in i]
        for i in profiles:
            try:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                try:
                    print ("{:<30}|  {:<}".format(i, results[0]))
                except :
                    print ("{:<30}|  {:<}".format(i, ""))
            except :
                print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))

def translate(text, src_lng=None, dest_lng=None):
    translator = Translator()
    if src_lng and dest_lng:
        translated = translator.translate(text, src=src_lng, dest=dest_lng)
    elif src_lng:
        translated = translator.translate(text, src=src_lng)
    elif dest_lng:
        translated = translator.translate(text, dest=dest_lng)
    else:
        translated =  translator.translate(text)

    return translated

    parser = argparse.ArgumentParser()
    parser.add_argument('text', type=str, help='text to translate')
    parser.add_argument('-s', '--src', default=None, help='origin language of the text')
    parser.add_argument('-d', '--dest', default=None, help='destiny language of the translation')
    parser.add_argument('-v', '--verbose', help='show more information', action='store_true')
    
    args = parser.parse_args()
    
    tr = translate(args.text, args.src, args.dest)
    
    if args.verbose:
        print('original text: %s' % tr.origin)
        print('translated text: %s' % tr.text)
        print('origin language: %s' % tr.src)
        print('destiny language: %s' % tr.dest)
    else:
        print(tr.text)

def installer():
    print("WARNING! Package Install Can't Operate Under Restricted Proxy...")
    print("Now Uninstalling Googletrans Package")
    os.system("pip uninstall googletrans")
    print("Now Installing Googletrans Package")
    print("Installing now...")
    os.system("pip install googletrans")
    print("If error thrown, update your Python or reinstall.")
    time.sleep(3)
    os.system('cls||clear')
    print("PyPrompt Closing in 5 Seconds")
    time.sleep(1)
    os.system('cls||clear')
    print("PyPrompt Closing in 4 Seconds")
    time.sleep(1)
    os.system('cls||clear')
    print("PyPrompt Closing in 3 Seconds")
    time.sleep(1)
    os.system('cls||clear')
    print("PyPrompt Closing in 2 Seconds")
    time.sleep(1)
    os.system('cls||clear')
    print("PyPrompt Closing in 1 Second")
    time.sleep(1)
    exit()

y = "1.4.1"

main(current_dir)
