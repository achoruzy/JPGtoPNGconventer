import sys
import os


# check if folder exists and create a folder if not
def createFolder(loc: str):
    try:
        return os.mkdir(loc)
    except FileExistsError:
        pass


# Loop over files in a folder
def genLoopOverFiles(folder: str):
    '''
    Generator for looping files in a folder. Yield a list [file, counter] with a file name and a counter (see below).
    The function posses additional counter for misc usage, starts at 0 for first file.
    '''
    counter = -1
    for file in os.listdir(folder):
        counter += 1
        yield [file, counter]
