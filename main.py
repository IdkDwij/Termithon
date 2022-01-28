import os

# Made in python, with pycharm
print('Termithon')
idkdwij = '''
    I   D       K   K   D       W         W     I       J
    I   D   D   K K     D  D    W    W    W     I   J   J
    I   D       K   K   D       W  W   W  W     I     J J
'''
print('The Python based terminal by' + idkdwij + 'it says idkdwij')
print('The source is here')

current_dir = os.getcwd()
commands = '''ls (shows files in current directory)
'''


class command:
    def boot(self):
        global cmd
        cmd = input(current_dir + '>')
        command().whatiscommand()

    def whatiscommand(self):
        if cmd == 'help':
            print(commands)
            command().boot()

        if cmd == 'ls':
            print(os.listdir(current_dir))
            command().boot()


command().boot()
