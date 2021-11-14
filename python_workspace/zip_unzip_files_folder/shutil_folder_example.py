'''
Compresses a folder into zip archive
'''
import shutil

shutil.make_archive(base_name='shutil_compr_folder',
                    format='zip', root_dir='folder')

shutil.unpack_archive(filename='shutil_compr_folder.zip',
                      extract_dir='shutil_extract_folder', format='zip')
