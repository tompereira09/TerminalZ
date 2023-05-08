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

def cat(path):
    file = open(path, "r")
    print("-------------------")
    print(file.read())
    print("-------------------")

def list():
    file = open("commands.txt", "r")
    print("-------------------")
    print(file.read())
    print("-------------------")

def search_command(target, curr):
    file = open("commands.txt", "r")
    contents = file.read().split("\n")
    curr = curr
    if curr == len(contents):
        print("Command Not Found.")
    elif contents[curr] == target:
        print("Command Found!")
    else:
        search_command(target, curr+1)
def clear():
    os.system('cls')
