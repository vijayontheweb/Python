'''
Extracts a zip archive into target location
'''
import zipfile
compr_file = zipfile.ZipFile('compr_file.zip', 'r')
compr_file.extractall('folder')
compr_file.close()
