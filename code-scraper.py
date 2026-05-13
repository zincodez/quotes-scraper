from bs4 import BeautifulSoup as bs
import requests
url=r'https://quotes.toscrape.com/'
data=requests.get(url).text
soup=bs(data,'lxml')
with open('quotes.txt','w') as fh:
    for quotes in soup.find_all('div',class_='quote'):
        fh.write(quotes.span.text+"\n")
        fh.write("by-" +quotes.small.text + '\n')