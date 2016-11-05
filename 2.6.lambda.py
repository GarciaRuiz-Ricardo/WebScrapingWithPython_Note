from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://pythonscraping.com/pages/page3.html'
request = urlopen(url)
bsObj = BeautifulSoup(request, 'lxml')

tag_2attr = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
for tag in tag_2attr:
    print(tag.get_text())