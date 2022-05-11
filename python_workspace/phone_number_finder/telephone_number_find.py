'''
You should now see 5 folders, each with a lot of random .txt files.
Within one of these text files is a telephone number formated ###-###-#### 
Use the Python os module and regular expressions to iterate through each file, open it, and search for a telephone number.
'''
import os
import shutil
import re

quantified_phone_pattern = r"\d{3}-\d{3}-\d{4}"
PATH = os.getcwd()
print(f'Current working directory -> {PATH}')
print('os.walk -> ')
print(list(os.walk(PATH)))
for path, sub_folders, files in os.walk(PATH):
    print(f'Currently looking at directory: {path}')
    print(f'Sub Folders are :')
    for folder in sub_folders:
        print(f'\tSub Folder: {folder}')
    print(f'Files are :')
    for filename in files:
        print(f'\t{filename}')
        fullpath = os.path.join(path, filename)
        with open(fullpath, 'r') as f:
            str = f.read()
            # print(str)
            matches = re.findall(quantified_phone_pattern, str)
            if(len(matches) == 0):
                print('\t\tNO MATCHES FOUND')
            for match in matches:
                print(f'\t\tFOUND MATCH -> {match}')
