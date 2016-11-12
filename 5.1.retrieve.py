from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.pythonscraping.com'
request = urlopen(url)
bsObj = BeautifulSoup(request, 'lxml')
imageLocation = bsObj.find('a', {'id': 'logo'}).find('img')['src']
# imageLocation = bsObj.find('a', {'id': 'logo'})
# print(imageLocation)
# imageLocation = bsObj.find('a', {'id': 'logo'}).find('img').attrs['src']
# print(imageLocation)
urlretrieve(imageLocation, '5.1.logo.jpg')
