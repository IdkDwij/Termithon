import os
import subprocess
import shlex
import string
from random import *
import curses
import time
from random import randint

# Made in python, with pycharm and OnlineGDB
# thanks for green1490#2863 for helping me with arguments
# Edited by joalricha869 to expand code

print('Termithon')
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
print('The Python based terminal by' + idkdwij + 'it says idkdwij')
print(" ")
print('Expanded by' + joalricha + 'it says joalricha')
print(" ")
print('The source is here')
print("Type in 'help' for the command list.")
print("")



def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


current_dir = os.getcwd()

commands = '''dir (Shows files in current directory)
cd (Go to specific directory in OS File System) (BETA STAGE DOESN'T WORK)
exit (Exits Termithron)
getmac (Retrieves the Physical MAC Address of The Device)
calc (A simple calculator)
passgen (A very efficient password generator)
'''


def cdCmd():
    print("This command sadly won't function in Python. Just here cuz it exists lol so no ")
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
    if cmd == 'help':
        print(commands)
        main()

    elif cmd == 'dir':
        print(os.listdir(current_dir))
        main()

    elif cmd == "cd":
        global args
        args = cmd
        cdCmd()
    elif cmd == 'exit':
        exit()
    elif cmd == 'getmac':
        getmac()
        main()
    elif cmd == "calc":
        calc()
        main()
    elif cmd == "passgen":
        passGen()
        main()
    else:
        print('invalid')
        main()


def main():
    global cmd
    cmd = input(current_dir + '>')
    whatiscommand()

def getmac():
    import re, uuid
    print ("The MAC address of this Device is : ", end="")
    print (':'.join(re.findall('..', '%012x' % uuid.getnode())))

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


lsdir = current_dir
main()



import os
import subprocess
import shlex
import string
from random import *
import curses
import time
from random import randint

# Made in python, with pycharm and OnlineGDB
# thanks for green1490#2863 for helping me with arguments
# Edited by joalricha869 to expand code

print('Termithon')
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
print('The Python based terminal by' + idkdwij + 'it says idkdwij')
print(" ")
print('Expanded by' + joalricha + 'it says joalricha')
print(" ")
print('The source is here')
print("Type in 'help' for the command list.")
print("")



def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


current_dir = os.getcwd()

commands = '''dir (Shows files in current directory)
cd (Go to specific directory in OS File System) (BETA STAGE DOESN'T WORK)
exit (Exits Termithron)
getmac (Retrieves the Physical MAC Address of The Device)
calc (A simple calculator)
passgen (A very efficient password generator)
'''


def cdCmd():
    print("This command sadly won't function in Python. Just here cuz it exists lol so no ")
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
    if cmd == 'help':
        print(commands)
        main()

    elif cmd == 'dir':
        print(os.listdir(current_dir))
        main()

    elif cmd == "cd":
        global args
        args = cmd
        cdCmd()
    elif cmd == 'exit':
        exit()
    elif cmd == 'getmac':
        getmac()
        main()
    elif cmd == "calc":
        calc()
        main()
    elif cmd == "passgen":
        passGen()
        main()
    else:
        print('invalid')
        main()


def main():
    global cmd
    cmd = input(current_dir + '>')
    whatiscommand()

def getmac():
    import re, uuid
    print ("The MAC address of this Device is : ", end="")
    print (':'.join(re.findall('..', '%012x' % uuid.getnode())))

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


lsdir = current_dir
main()




