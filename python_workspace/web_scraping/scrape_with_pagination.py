'''
https://books.toscrape.com/ - practice grabbing elements across multiple pages
Get title of every book with a four star rating
'''
import requests
import bs4

url_template = 'https://books.toscrape.com/catalogue/page-{}.html'
for page_num in range(1, 51):
    current_url = url_template.format(str(page_num))
    result = requests.get(current_url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    product_pods = soup.select('.product_pod')
    for product_pod in product_pods:
        if(len(product_pod.select('.star-rating.Three')) == 1):
            print(product_pod.select('h3 > a')[0]['title'])
            print(
                '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
