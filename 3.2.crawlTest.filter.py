from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = 'https://en.wikipedia.org/wiki/Kevin_Bacon'
request = urlopen(url)
bsObj = BeautifulSoup(request, 'lxml')

for link in bsObj.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])