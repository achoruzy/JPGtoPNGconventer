from PIL import Image
import os


def fileConvert(file_from: str, folder_to: str, out_file_name: str, format_to: str):
    '''
    Converts an image file to chosen format.
    '''
    if os.path.isfile(file_from):
        with Image.open(file_from, mode='r') as img:
            file_out = folder_to + out_file_name + '.' + format_to
            return img.save(file_out, format=format_to)
