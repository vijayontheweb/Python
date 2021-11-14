import requests
import bs4

result = requests.get(
    'https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(result.text, 'lxml')
print(soup.select('img')[0])

image_link = requests.get(
    'https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
# print(image_link.content)
with open('my_computer_image.jpg', 'wb') as f:  # wb -> write binary
    f.write(image_link.content)
