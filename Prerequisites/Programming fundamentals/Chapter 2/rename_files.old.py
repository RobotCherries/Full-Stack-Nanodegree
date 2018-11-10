# This is a program that renames all the files within a folder so that they do not have any numbers in their title

import os

def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir(r'C:\Users\oana\Documents\Udacity\Full Stack Nanodegree\Programming fundamentals\prank')
    # print(file_list)

    # (2) for each file, rename filename
    for file_index in range(len(file_list)):

        filename = file_list[file_index]
        new_filename = ''
        
        # (3) for each letter in the filename
        for char in filename:
            # (4) check if it's not a number and strore it in the new_filename
            if(not char.isdigit()):
                print(char)
                new_filename += char
                print(new_filename)
        # (5) use the new_filename to replace the old filename
        os.renames(r'C:\\Users\oana\\Documents\\Udacity\\Full Stack Nanodegree\\Programming fundamentals\prank\\' + filename, r'C:\\Users\\oana\Documents\\Udacity\\Full Stack Nanodegree\\Programming fundamentals\\prank\\' + new_filename)
        file_index = file_index + 1
    print(os.listdir)
            

rename_files()