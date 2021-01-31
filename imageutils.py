from PIL import Image


def fileConvert(file_from: str, folder_to: str, file_name: str, format_to: str):
    '''
    Converts chosen image file to chosen format.
    '''
    with Image.open(file_from, mode='r') as img:
        file_out = folder_to + file_name + '.' + format_to
        img.save(file_out, format=format_to)


if __name__ == "__main__":
    pass
