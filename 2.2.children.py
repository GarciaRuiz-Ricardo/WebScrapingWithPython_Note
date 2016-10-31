from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://pythonscraping.com/pages/page3.html'
request = urlopen(url)
bsObj = BeautifulSoup(request)

print('--- children ---')
for child in bsObj.find('table', {'id':'giftList'}).children:
    print(child)

