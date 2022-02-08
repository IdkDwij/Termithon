import os
import socket
import getpass
from uuid import getnode as get_mac
mac = get_mac()
import string
from random import *
import time
from random import randint
import socket
import platform
import subprocess
import re
import uuid
# Made in python
# collaborated with https://github.com/BigBoyTaco/ for this little update
# Made in Python, with PyCharm and OnlineGDB
# Compiled on desktop in Visual Studio 2019
# Thanks for green1490#2863 for helping me with arguments
# Edited by joalricha869 to expand code

print("="*40, "Termithron 2.0", "="*40)
idkdwij = '''
    I   D       K   K   D       W         W     I       J
    I   D   D   K K     D  D    W    W    W     I   J   J
    I   D       K   K   D       W  W   W  W     I     J J
'''
joalricha = '''
    J    OOO    AAA   L    RRRR   I   CCC  H  H   AAA
    J   O   O  A   A  L    R   R  I  C     HHHH  A   A
    J   O   O  AAAAA  L    RRRR   I  C     H  H  AAAAA
  JJJ    OOO   A   A  LLL  R   R  I   CCC  H  H  A   A
'''
print('The Python based terminal by:' + idkdwij + 'it says idkdwij tho')
print(" ")
print('Expanded by:' + joalricha + 'it says joalricha')
print(" ")
print('The source is here')
print("Type in 'help' for the command list.")
print("")

hostname = socket.gethostname()

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


current_dir = os.getcwd()

commands = '''dir (Shows files in current directory)
exit (Exits Termithron)
ip (Gives you your IP)
hostname (Gives you your Computer's ID)
mac (Retrieves the Physical MAC Address of The Device)
ping (lets you ping a website)
calc (A simple calculator)
passgen (A very efficient password generator)
sysinfo (Gets relevant system info)
ver (Reports Termithron Version)
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
    elif cmd == 'dir':
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
        print("Your IP Address is " + getip())
        main()
    #hostname command
    elif cmd == 'hostname':
        uname = platform.uname()
        print(hostname)
        main()
    elif cmd == "mac":
        getmac()
        main()
    elif "ping" in cmd:
        os.system(cmd)
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
    else:
        error()


def main():
    global cmd
    cmd = input(current_dir + '>')
    whatiscommand()

def ver():
    print("Termithron 2.3")
    print("(C) 2022 joalricha869, idkDwij All Rights Reserved.")

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

def error():
    print("'" + str(cmd) + "'" + ''' is not recognized as an internal or external command''')
    main()

        


main()
