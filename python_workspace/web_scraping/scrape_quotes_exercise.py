'''
1. Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ 
and get the HTML text from the homepage.
2. Get the names of all the authors on the first page.
3. Create a list of all the quotes on the first page.
4. Inspect the site and use Beautiful Soup to extract the top ten tags from the requests 
text shown on the top right from the home page (e.g Love,Inspirational,Life, etc...). 
HINT: Keep in mind there are also tags underneath each quote, try to find a class only 
present in the top right tags, perhaps check the span.
5. Notice how there is more than one page, and subsequent pages look like this 
http://quotes.toscrape.com/page/2/. Use what you know about for loops and string concatenation 
to loop through all the pages and get all the unique authors on the website. Keep in mind 
there are many ways to achieve this, also note that you will need to somehow figure out how to 
check that your loop is on the last page with quotes. For debugging purposes, I will let you 
know that there are only 10 pages, so the last page is http://quotes.toscrape.com/page/10/, 
but try to create a loop that is robust enough that it wouldn't matter to know the amount of 
pages beforehand, perhaps use try/except for this, its up to you!
'''
import requests
import bs4

# Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/
# and get the HTML text from the homepage.
url_template = 'https://quotes.toscrape.com/page/{}/'
current_url = url_template.format(str(1))
result = requests.get(current_url)
soup = bs4.BeautifulSoup(result.text, 'lxml')
print(soup)
print('++++++++++++++++++++++++++++++++++++++++++++++++')
# Get the names of all the authors on the first page.
quotes = soup.select('.quote')
for quote in quotes:
    print(quote.select('span > small')[0].get_text())
print('++++++++++++++++++++++++++++++++++++++++++++++++')
# Create a list of all the quotes on the first page.
for quote in quotes:
    print(quote.select('span')[0].get_text())
print('++++++++++++++++++++++++++++++++++++++++++++++++')
# Inspect the site and use Beautiful Soup to extract the top ten tags from the requests
# text shown on the top right from the home page (e.g Love,Inspirational,Life, etc...).
# HINT: Keep in mind there are also tags underneath each quote, try to find a class only
# present in the top right tags, perhaps check the span.
tag_items = soup.select('.tag-item')
for tag_item in tag_items:
    print(tag_item.select('a')[0].get_text())
print('++++++++++++++++++++++++++++++++++++++++++++++++')
# Notice how there is more than one page, and subsequent pages look like this
# http://quotes.toscrape.com/page/2/. Use what you know about for loops and string concatenation
# to loop through all the pages and get all the unique authors on the website. Keep in mind
# there are many ways to achieve this, also note that you will need to somehow figure out how to
# check that your loop is on the last page with quotes. For debugging purposes, I will let you
# know that there are only 10 pages, so the last page is http://quotes.toscrape.com/page/10/,
# but try to create a loop that is robust enough that it wouldn't matter to know the amount of
# pages beforehand, perhaps use try/except for this, its up to you!
page_num = 1
page_exist = True
unique_authors = set()
while(page_exist):
    current_url = url_template.format(str(page_num))
    result = requests.get(current_url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    quotes = soup.select('.quote')
    for quote in quotes:
        unique_authors.add(quote.select('span > small')[0].get_text())
    if(soup.select('.next') == []):
        page_exist = False
    else:
        page_num += 1
print(unique_authors)
