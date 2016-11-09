from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now)

def getLinks(articleUrl):
    url = 'https://en.wikipedia.org'+articleUrl
    request = urlopen(url)
    bsObj = BeautifulSoup(request, 'lxml')
    links = bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href = re.compile('^(/wiki/)((?!:).)*$'))
    return links

links = getLinks('/wiki/Kevin_Bacon')
# for link in links:
#     print(link.attrs['href'])
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)