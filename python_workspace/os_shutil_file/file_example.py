import os
import shutil

f = open('practice1.txt', 'w+')
f.write('Some text here')
f.close()
f = open('practice2.txt', 'w+')
f.write('Another text here')
f.close()

print(os.getcwd())
print(os.listdir())
print(os.listdir('C:\\Users'))
shutil.move('practice1.txt', 'myfolder\\practice1.txt')
os.unlink('practice2.txt')

print(os.getcwd())
for folder, sub_folders, files in os.walk(os.getcwd()):
    print(f'Currently looking at Directory: {folder}')
    print(f'Sub Folders are :')
    for folder in sub_folders:
        print(f'\tSub Folder: {folder}')
    print(f'Top level files are :')
    for file in files:
        print(f'\tTop Level Files: {file}')
