import utils
import config
import colorama
import os
import sys
from pathlib import Path

config_obj = config.Config()
path = config_obj.get_path()
version = config_obj.get_version()

print(colorama.Fore.GREEN + f'Welcome to TerminalZ!\nVersion Number: {version}' + colorama.Fore.WHITE)

run = True
while run:
    curr_inp = input(f'TZ {path}> ')
    inp_list = curr_inp.split(" ")
    if curr_inp == "ls":
        utils.ls(path)
    elif inp_list[0] == "cd":
        if len(inp_list) > 1:
            if inp_list[1] != "..":
                if len(inp_list) == 2:
                    try:
                        print("Option 1")
                        dir = inp_list[1]
                        os.chdir(dir)
                        path = os.getcwd()
                    except Exception as e:
                        print(colorama.Fore.RED + f'Error finding dir: {e}' + colorama.Fore.WHITE)
                else:
                    try:
                        dir = inp_list[1:]
                        new_dir = " ".join(dir)
                        os.chdir(new_dir)
                        path = os.getcwd()
                    except Exception as e:
                        print(colorama.Fore.RED + f'Error finding dir: {e}' + colorama.Fore.WHITE)
            elif inp_list[1] == "..":
                back_path = Path(path)
                os.chdir(back_path.parent.absolute())
                path = os.getcwd()
        else:
            print(colorama.Fore.RED + "Error: 'cd' must take an argument." + colorama.Fore.WHITE)
