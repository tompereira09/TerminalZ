import os
import sys
import colorama
from colorama import Fore, Back, Style

path = os.getcwd()

def ls(path):
    files = os.listdir(path)
    for file in files:
        if "." in file:
            new_file = file.split(".")
            if len(new_file) == 2:
                print(file)
        else:
            print(Fore.GREEN + file + Fore.WHITE)

