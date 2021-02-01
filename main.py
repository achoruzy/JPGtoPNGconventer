import sys
import utilities as util
import window as win
import imageutils as imut

folder_from = sys.argv[1]
folder_to = sys.argv[2]
format_to = sys.argv[3]
new_file_name = 'new_'


if __name__ == "__main__":

    util.createFolder(folder_to)
    for i in util.genLoopOverFiles(folder_from):
        imut.fileConvert(
            folder_from + str(i[0]), folder_to, new_file_name + str(i[1]), format_to)
    print('>>> DONE! <<<')
