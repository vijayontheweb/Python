import requests
import bs4

result = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(result.text, 'lxml')
print(soup.select('.toclevel-1.tocsection-1')
      [0].select('.toctext')[0].get_text())
