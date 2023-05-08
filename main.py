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
            print(colorama.Fore.RED + "Error: 'cd' must take one argument." + colorama.Fore.WHITE)
    elif inp_list[0] == "cat":
        if len(inp_list) == 2:
            try:
                utils.cat(inp_list[1])
            except Exception as e:
                print(colorama.Fore.RED + f'Error finding file: {e}' + colorama.Fore.WHITE)
        else:
            print(colorama.Fore.RED + "Error: 'cat' must take one argument." + colorama.Fore.WHITE)

    elif curr_inp == "list":
        utils.list()
    elif inp_list[0] == "find":
        if len(inp_list) == 2:
            try:
                utils.search_command(inp_list[1], 0)
            except Exception as e:
                print(colorama.Fore.RED + f'Error: {e}' + colorama.Fore.WHITE)
        else:
            print(colorama.Fore.RED + "Error: 'cat' must take one argument." + colorama.Fore.WHITE)

    elif curr_inp == "clear":
        utils.clear()

