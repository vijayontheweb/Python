'''
Compresses a set of files into zip archive
'''
import zipfile

f = open('file1.txt', 'w+')
f.write('content')
f.close()

f = open('file2.txt', 'w+')
f.write('content')
f.close()

compr_file = zipfile.ZipFile('compr_file.zip', 'w')
compr_file.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED)
compr_file.write('file2.txt', compress_type=zipfile.ZIP_DEFLATED)
compr_file.close()
