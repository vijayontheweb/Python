import requests
import bs4

result = requests.get('https://www.example.com/')
print(type(result))  # <class 'requests.models.Response'>
# print(result.text)  # content similar to view source
soup = bs4.BeautifulSoup(result.text, 'lxml')
print(soup)  # formatted content similar to view source
# [<title>Example Domain</title>] -> Returns as an array with tag and text as
# technically there could be more than one element on this page
print(soup.select('title'))
# Example Domain -> Just the title alone
print(soup.select('title')[0].get_text())
print(soup.select('p'))  # grab all paragraphs
print(soup.select('p')[0].get_text())  # grab first paragraph
