from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://pythonscraping.com/pages/page3.html'
request = urlopen(url)
bsObj = BeautifulSoup(request)

print('--- sibling ---\n')
for sibling in bsObj.find('table',{'id':'giftList'}).tr.next_siblings:
    print(sibling)