from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://pythonscraping.com/pages/page3.html'
request = urlopen(url)
bsObj = BeautifulSoup(request)

price = bsObj.find('img',{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text()
print(price)