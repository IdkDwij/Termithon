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
import time
import shutil
import sys
import argparse
import re
from time import sleep
import urllib.request
try:
    import speedtest
    import geocoder
    import paramiko
except:
    print("Speedtest Package Not Found")
    print("Installing Now...")
    os.system("pip install speedtest-cli")
    os.system('cls||clear')
    print("Geocoder Package Not Found")
    print("Installing Now...")
    os.system("pip install geocoder")
    os.system("cls||clear")
    print("Paramiko Package Not Found")
    print("Installing Now...")
    os.system("pip install paramiko")
    os.system("cls||clear")
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
print('Based on Termithon by' + dwij + 'https://github.com/IdkDwij/Termithon')
print(" ")
print("The source is at my GitHub page! 'https://github.com/joalricha869/PyPrompt'")
print("Type in 'help' for the command list.")
print("")
hostnamecomputer = socket.gethostname()
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
20. cd (Navigate through folders)
21. iplocation (Find the physical location of your IP address)
22. speedtest (Speedtest.net but built into PyPrompt!)
23. encryptdecrypt (Uses the RSA Algorithm to encrypt and decrypt a message!)
24. troubleshoot (Troubleshoots extra modules neccessary for PyPrompt to run)
25. ssh (An SSH Client made in Python) DO NOT USE THIS TOOL FOR ILLEGAL PURPOSES!
26. macosdownloader (gibMacOS but made as a function for use in PyPrompt)

(There's an easter egg in form of a command! Try to find it!) hint: help but not help (un is in the word)

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
        print(hostnamecomputer)
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
    elif cmd == "speedtest":
        speedtestapp()
        main(current_dir)
    elif cmd == "iplocation":
        iplocation()
        main(current_dir)
    elif "encryptdecrypt" in cmd:
        encryptdecrypt()
        main(current_dir)
    elif cmd == "unhelp":
        print("The command is 'ignore'")
        main(current_dir)
    elif cmd == "troubleshoot":
        troubleshoot()
        main(current_dir)
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
    elif cmd == "ssh":
        sshclient()
    elif cmd == "macosdownloader":
            macOSDownloader()
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
    print('Based on Termithon Shell by' + dwij + 'https://github.com/IdkDwij/Termithon')
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
    print("Search up BigBoyTaco Studios on YouTube for a tutorial on Termithon")

def speedtestapp():
    speed=speedtest.Speedtest()
    option=int(input('''
    What do you want to know:
    1) Download speed
    2) Upload speed
    3) Both Download and Upload
    4) Ping
    Your choice: '''))

    if option<1 or option>4:
        sleep(2)
        print('You have entered wrong choice, please enter again with values from 1 to 4')
    else:
        sleep(1)
        print()
        print('Pls wait, test in progress...')
        print()  
        down_speed=round(speed.download()/1000000,3)
        up_speed=round(speed.upload()/1000000,3)
        print('One more sec please...')
        sleep(2.5)
        print()
        if option == 1:
            print('Your Download speed is: ',down_speed,'Mbps')
        elif option == 2:
            print('Your Upload speed is: ',up_speed,'Mbps')
        elif option == 3:  
            print('Your Download speed is: ',down_speed,'Mbps',end=" ")
            print(',and your Upload speed is: ',up_speed,'Mbps')

        elif option == 4:
            s=[]
            speed.get_servers(s)
            print(speed.results.ping,'ms')
        else:
            print('Sorry, something went wrong, pls try again...')

def iplocation():
    g = geocoder.ipinfo('me')
    print(g.latlng)

def encryptdecrypt():
    def isPrime(n):
        prime = [True for i in range(n+1)]
        p = 2
        while p*p<=n:
            if prime[p]==True:
                for i in range(p*p,n+1,p):
                    prime[i]=False
            p+=1

        return prime[n]


    def gcd(a,b):
        while b!=0:
            r = a%b
            a=b
            b=r
        return a

    def Multiplicative_inverse(a,b):
        s1 = 1
        s2 = 0
        m = b
        while b!=0:
            q=a//b
            r=a%b
            a=b
            b=r
            s=s1-q*s2
            s1=s2
            s2=s
            
        if s1<0:
            s1+=m
            
        return s1

    def powermod(x,y,p):
        res = 1
        
        x = x%p 
        while (y>0):
            
            if (y%2) == 1:
                res = (res*x)%p
                
            y = y//2
            x = (x*x)%p
            
        return res

    if __name__ == '__main__':
        while (True):
            res = input('Do you want to enter prime numbers (y) or let the algorithm do it for you (n) or exit (e)? (y/n/e): ')
            if res == 'y':
                while True:
                    p = 13
                    p = int(input('Enter a prime number: '))
                    if isPrime(p):
                        break
                    else:
                        print(p,'is not a prime number')
                        continue

                while True:
                    q = 17
                    q = int(input('Enter a different prime number: '))
                    if isPrime(q) and (p*q>26):
                        break
                    else:
                        print('Both the prime numbers are same!! or product of both the prime numbers is less than 26!!')
                        continue

                n = p*q
                phi_n = (p-1)*(q-1)
                a = 19
                while True:
                    a = int(input('Enter a number such that Greatest Common Divisor of that number with '+ str(phi_n) + ' is 1: '))
                    if gcd(a,phi_n)!=1:
                        continue
                    else:
                        break

                b = Multiplicative_inverse(a,phi_n)
                message = input('Enter the message to be encrypted (lower case): ')
                message = message.lower()

                encrypted_string = ""
                encrypted_num = []

                for i in range(len(message)):
                    ch = message[i]
                    if ch!=' ':
                        m = ord(ch) - 97
                        e = powermod(m,a,n)
                        encrypted_num.append(e)
                        encrypted_string += chr(e%26 + 97)
                    else:
                        encrypted_string +=' '

                print('Encrypted message is:', encrypted_string)
                print(encrypted_num)
                res = input("Do you want to decrypt it too? (y/n): ")
                if res == 'y':
                    decrypted = ''
                    j=0
                    for i in range(len(encrypted_string)):
                        ch = message[i]
                        if ch != ' ':
                            e = encrypted_num[j]
                            m = powermod(e,b,n)
                            ch = chr(m+97)
                            decrypted+=ch
                            j+=1
                        else:
                            decrypted+=' '
                        
                    print("Decrypted message is:",decrypted)
                else:
                    ans = input("Do you want to continue? (y/n): ")
                    if ans == 'y':
                        continue
                    else:
                        break

            elif res == 'n':
                p = 13
                q = 17
                n = p*q
                a = 5
                b = 77
                message = input('Enter the message to be encrypted (lower case): ')
                message = message.lower()

                encrypted_string = ""
                encrypted_num = []

                for i in range(len(message)):
                    ch = message[i]
                    if ch!=' ':
                        m = ord(ch) - 97
                        e = powermod(m,a,n)
                        encrypted_num.append(e)
                        encrypted_string += chr(e%26 + 97)
                    else:
                        encrypted_string +=' '

                print('Encrypted message is:', encrypted_string)
                res = input("Do you want to decrypt it too? (y/n): ")
                if res == 'y':
                    decrypted = ''
                    j=0
                    for i in range(len(encrypted_string)):
                        ch = encrypted_string[i]
                        if ch != ' ':
                            e = encrypted_num[j]
                            m = powermod(e,b,n)
                            ch = chr(m+97)
                            decrypted+=ch
                            j+=1
                        else:
                            decrypted+=' '
                        
                    print("Decrypted message is:",decrypted)
                else:
                    ans = input("Do you want to continue? (y/n): ")
                    if ans == 'y':
                        continue
                    else:
                        break
            elif res == 'e':
                break
            else:
                print('Invalid command!')
                continue

def troubleshoot():
    confirmation = input("Troubleshoot Modules? ")
    if confirmation == "yes":
        print("Uninstalling Speedtest")
        os.system("pip uninstall speedtest-cli")
        os.system("cls||clear")
        print("Uninstalling geocoder")
        os.system("pip uninstall geocoder")
        os.system("cls||clear")
        print("Uninstalling paramiko")
        os.system("pip uninstall paramiko")
        os.system("cls||clear")
        print("Unins")
        print("Now Reinstalling Modules")
        print("Installing Speedtest")
        os.system("pip install speedtest-cli")
        os.system("cls||clear")
        print("Installing geocoder")
        os.system("pip install geocoder")
        os.system("cls||clear")
        print("Installing paramiko")
        os.system("pip install paramiko")
        os.system("cls||clear")
        print("Installing Scripts")
        os.system("pip install Scripts")
        os.system("cls||clear")
        os.system("cls||clear")
        print("PyPrompt Closing in 3 seconds")
        os.system("cls||clear")
        print("PyPrompt Closing in 2 seconds")
        os.system("cls||clear")
        print("PyPrompt Closing in 1 second")
        exit()

def sshclient():
    print("This may have compatability issues with earlier versions of Python.")
    print("Make sure you have Python 3.9 or later!")
    print("DISCLAIMER: This software can't be used for any type of illegal activity.")
    print("What you do here is now your OWN RESPONSIBILITY!!!")
    hostname = input("Enter hostname: ")
    port = input("Enter Port: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command('ifconfig')
    print(stdout.read())
    s.close()
    main()

def macOSDownloader():
    print("macOS Downloader")
    print("This downloader retrieves the files from Apple's official server and will download them using this command")
    print("1) macOS Monterey 12.3.1 (IPSW Version M1) (Requires a Real Mac)")
    print("2) macOS Monterey 12.2 (Requires a Real Mac)")
    print("3) macOS Monterey 12.1 (IPSW Version) (Requires a Real Mac)")
    print("4) macOS Big Sur 11.6.5 (Requires a Real Mac)")
    print("5) macOS Big Sur 11.6 (IPSW Version) (Requires a Real Mac)")
    print("6) macOS Catalina 10.15 (Requires a Real Mac)")
    print("7) macOS Catalina Patcher (Not from Apple)")

    versionSelecter = input("Which version of macOS do you want to download?: ")
    if versionSelecter == "1":
        urllib.request.urlretrieve("https://updates.cdn-apple.com/2022SpringFCS/fullrestores/002-79219/851BEDF0-19DB-4040-B765-0F4089D1530D/UniversalMac_12.3.1_21E258_Restore.ipsw", "Monterey12.3.1M1.ipsw")
        main(current_dir)
    elif versionSelecter == "2":
        urllib.request.urlretrieve("https://swcdn.apple.com/content/downloads/41/34/002-57041-A_P59UQKRDXZ/h73bziwp3o4m5kuk3ool1g55vgplpmkwqv/InstallAssistant.pkg", "Monterey12.2.pkg")
        main(current_dir)
    elif versionSelecter == "3":
        urllib.request.urlretrieve("https://updates.cdn-apple.com/2022WinterFCS/fullrestores/002-66272/FB0B40F5-49EB-421B-81EC-8B56B8468D3C/UniversalMac_12.2.1_21D62_Restore.ipsw", "Monterey12.1M1.ipsw")
        main(current_dir)
    elif versionSelecter == "4":
        urllib.request.urlretrieve("https://swcdn.apple.com/content/downloads/15/10/002-77154-A_LAKRVPO4Y6/dbmkv9538dfpvqaqdygjciw8775qjuytbh/InstallAssistant.pkg", "BigSur11.6.5.pkg")
        main(current_dir)
    elif versionSelecter == "5":
        urllib.request.urlretrieve("https://updates.cdn-apple.com/2021FallFCS/fullrestores/071-97388/C361BF5E-0E01-47E5-8D30-5990BC3C9E29/UniversalMac_11.6_20G165_Restore.ipsw", "BigSur11.6M1.ipsw")
        main(current_dir)
    elif versionSelecter == "6":
        urllib.request.urlretrieve("http://swcdn.apple.com/content/downloads/61/56/041-83630-A_8RCIBB415Y/7jqh3nh97ood2mjej7hdgpx7fgh5c3fi9g/InstallESDDmg.pkg", "Catalina10.5.pkg")
        main(current_dir)
    elif versionSelecter == "7":
        print("Go to this website!")
        print("http://dosdude1.com/catalina/")
        main(current_dir)
        

y = "1.4.4"

main(current_dir)


