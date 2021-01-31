import sys
import os
import window as win
import utilities as util
import imageutils as imut

folder_from = sys.argv[1]
folder_to = sys.argv[2]
format_to = sys.argv[3]

# Loop over files in folder


def loopOverFiles():
    counter = 0
    for filename in os.listdir(folder_from):
        counter += 1
        imut.fileConvert(folder_from + filename, folder_to,
                         str(counter), format_to)


if __name__ == "__main__":
    loopOverFiles()
