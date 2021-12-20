import os
import shutil
import sys
from datetime import datetime


# Creates a folder tree of
# 2021 -> [01,02,03,...]
# 2022 -> [01,02,03,...]
# etc.
def create_year_month_folder_tree(path, start_year):
    """
    :param path: The directory where all the individual files are located in the form of a str
    :param start_year: The year of the earliest file in the directory
    :return: N/A
    """
    if not os.path.isdir(path):
        sys.exit("Exit: Path Does Not Exist.")
    else:
        for year in range(start_year, datetime.now().year + 1):
            if not os.path.isdir(os.path.join(path, str(year))):
                os.mkdir(os.path.join(path, str(year)))
            for month in range(1, datetime.now().month + 1):
                if not os.path.isdir(os.path.join(path, str(year), str(month).rjust(2, '0'))):
                    os.mkdir(os.path.join(path, str(year), str(month).rjust(2, '0')))


def org_dated_files(path, ):
    """

    :param path:
    :return:
    """
    if not os.path.isdir(path):
        sys.exit("Exit: Path Does Not Exist.")
    else:
        dir_contents = sorted([f for f in os.listdir(path)], key=lambda f: f.lower())
        dir_contents = [f for f in dir_contents if not f.startswith('.')]
        dir_contents = [f for f in dir_contents if not f == 'Icon\r']
        for i in dir_contents:
            if not os.path.isdir(os.path.join(path, i)):
                if os.path.isfile(os.path.join(path, str(i))):
                    print(i)
                # print(type(i))
                # print(f'{i}')
                try:
                    j = i.split('-')
                    # print(os.path.join(path,i))
                    # print(os.path.join(path,j[0],j[1],i))
                    dest = shutil.move(os.path.join(path, i), os.path.join(path, j[0], j[1], i))
                    print(dest)
                except:
                    pass


def delete_empty_folders(path, start_year):
    """
    
    :param path: 
    :param start_year: 
    :return: 
    """
    if not os.path.isdir(path):
        sys.exit()

    # empties out all month folders with nothing in them.
    # layer 2
    # this ensures that all folders with only empty folders in it are erased properly.
    for year in range(start_year, datetime.now().year + 1):
        for i in os.walk(os.path.join(path, str(year))):
            # print(i)
            if not i[1] and not i[2]:
                # print(i[0])
                os.rmdir(i[0])

    # empties out all year folders with nothing in them.
    # top layer
    for i in os.walk(path):
        if not i[1] and not i[2]:
            os.rmdir(i[0])
            # print(i)


def organize_files(path,start_year):
    """
    :param path:
    :param start_year:
    :return:
    """
    create_year_month_folder_tree(path, start_year)
    org_dated_files(path)
    delete_empty_folders(path, start_year)


if __name__ == '__main__':
    path = '/Users/chaseallbright/Dropbox/Camera Uploads'
    start_year = 2010
    organize_files(path, start_year)
