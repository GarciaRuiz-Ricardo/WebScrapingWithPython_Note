from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = 'http://pythonscraping.com/pages/page3.html'
request = urlopen(url)
bsObj = BeautifulSoup(request, 'lxml')

# images = bsObj.findAll('img',{'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
images = bsObj.findAll('img',{'src':re.compile('\.\./img/gifts/img.*\.jpg')})
for image in images:
    print(image)