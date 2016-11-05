from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Kevin_Bacon'
request = urlopen(url)
bsObj = BeautifulSoup(request, 'lxml')

for link in bsObj.findAll('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])