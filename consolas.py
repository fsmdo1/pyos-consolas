import pystream
import os
import shutil
import hfmi

working_directory = os.getcwd()

def ls():
    global working_directory
    listdir = os.listdir(working_directory)
    for i in listdir:
        print(i)

def cd():
    global working_directory
    pathdir = input("Path: ")
    fullpath = working_directory + "/" + pathdir
    isdir = os.path.isdir(fullpath)
    if (isdir == True):
        working_directory = fullpath
    else:
        print("Directory not found.")

def cddotdot():
    global working_directory
    working_directory = os.path.abspath(os.path.join(working_directory, os.pardir))

def pwd():
    global working_directory
    print(working_directory)

def mkdir():
    path = working_directory + "/" + input("Path: ")
    if not os.path.exists(path):
        os.mkdir(path)

def loadmod():
    modpath = input("Please, enter mod path.")
    with open(modpath) as f2:
        exec(f2.read())

# Compact HFMI included

def hfmi():
    hfmi.function_select()

#########################
    
def help():
    print("ls - Show directory entries")
    print("hfmi - Humanity FileManager Improved")
    print("m - Load mod")
    print("help - Show this help message")
    print("exit - Exit PyOS")

def exit():
    sys.exit()
commands = {
    "ls":ls,
    "cd":cd,
    "cd ..":cddotdot,
    "pwd":pwd,
    "mkdir":mkdir,
    "hfmi":hfmi,
    "m":loadmod

}