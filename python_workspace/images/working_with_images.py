from PIL import Image

img = Image.open('example.jpg')
print(type(img))    # <class 'PIL.JpegImagePlugin.JpegImageFile'>
# img.show()  # displays image in gallery
print(img.size)  # (1993, 1257)
print(img.filename)  # example.jpg
print(img.format_description)   # JPEG (ISO 10918)
# img.crop((0, 0, 500, 500)).show()
img = Image.open('pencils.jpg')
x = 0
y = 0
width = 200
height = 300
# crop image
#img.crop((x, y, width, height)).show()
halfway = 1993/2
height = 1257
x = halfway - 200
width = halfway + 200
y = 800
cropped_mac = Image.open('example.jpg').crop((x, y, width, height))
# cropped_mac.show()
# copy and paste
Image1 = Image.open('purple.png')
Image1copy = Image1.copy()
print(Image1copy.size)
Image2 = Image.open('blue_color.png')
Image2copy = Image2.crop((0, 0, 50, 50)).copy()
print(Image2copy.size)
Image1copy.paste(Image2copy, (12, 12))
Image1copy.paste(Image2copy, (72, 12))
Image1copy.paste(Image2copy, (135, 12))
Image1copy.paste(Image2copy, (12, 72))
Image1copy.paste(Image2copy, (12, 135))
Image1copy.paste(Image2copy, (72, 72))
Image1copy.paste(Image2copy, (72, 135))
Image1copy.paste(Image2copy, (135, 135))
Image1copy.paste(Image2copy, (135, 72))
Image1copy.save('remix.png')
# resize an image
Image.open('example.jpg').resize((1000, 500)).show()
# rotate an image
Image.open('example.jpg').rotate(90).show()
# Color Transparency. Alpha range 0-255
purple_img = Image.open('purple.png')
red_img = Image.open('red_color.jpg')
red_img_copy = red_img.copy()
red_img_copy.putalpha(100)
red_img_copy.show()
red_img_copy.save('red_color_alpha.png')

purple_img_copy = purple_img.copy()
purple_img_copy.putalpha(100)
purple_img_copy.show()
purple_img_copy.save('purple_color_alpha.png')

red_img.paste(im=purple_img_copy, box=(0, 0), mask=purple_img_copy)
red_img.save('purple_red_alpha_remix.png')
