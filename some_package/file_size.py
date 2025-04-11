
from os import listdir
from os.path import isfile, join
import os


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        # return convert_bytes(file_info.st_size)
        return file_info.st_size


def print_file_names(files):
    for n in files:
        print(n)

# Lets check the file size of MS Paint exe 
# or you can use any file path

if __name__=="__main__":
    directory_path = "D:\\Репететирство\\Всеволод\\"
    file_path = "D:\\Репететирство\\Всеволод\\DEMO-12.rar"
    onlyfiles = [f for f in listdir(directory_path) if isfile(join(directory_path, f))]
    print_file_names(onlyfiles)
    print(file_size(file_path))