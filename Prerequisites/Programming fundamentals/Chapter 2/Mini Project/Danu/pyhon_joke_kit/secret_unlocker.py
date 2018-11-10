# This is a program that renames all the files within a folder so that they do not have any numbers in their title

import os


def rename_files():
    # (1) get file names from a folder
    curr_dir = os.getcwd()
    file_list = os.listdir(curr_dir + '\\secret')
    
    os.chdir(curr_dir + '\\secret')

    # (2) for each file, rename filename
    for filename in file_list:
        new_filename = filename.translate(str.maketrans('', '', '0123456789'))
        print('Old filename - ' + filename)
        print('New filename - ' + new_filename)
        os.rename(filename, new_filename)

    print(os.listdir)
    os.chdir(curr_dir)


rename_files()
