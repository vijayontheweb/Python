'''
there are two images we will be working with: 1)word_matrix.png 2)mask.png
The word_matrix is a .png image that contains a spreadsheet of words with a hidden message in it.
Your task is to use the mask.png image to reveal the hidden message inside the word_matrix.png. 
Keep in mind, you may need to make changes to the mask.png in order for this to work.

Solution: Enlarge the mask to the size of the word matrix
'''

from PIL import Image

mask_img = Image.open('mask.png')
word_matrix_img = Image.open('word_matrix.png')
print(mask_img.size)
print(word_matrix_img.size)
mask_img_copy = mask_img.copy().resize((1015, 559))
word_matrix_img_copy = word_matrix_img.copy()
word_matrix_img_copy.putalpha(50)
mask_img_copy.paste(im=word_matrix_img_copy, box=(0, 0),
                    mask=word_matrix_img_copy)
mask_img_copy.save('secret_words.png')
