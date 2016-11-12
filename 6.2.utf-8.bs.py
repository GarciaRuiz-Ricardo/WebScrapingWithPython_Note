from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://en.wikipedia.org/wiki/Python_(programming_language)'
request = urlopen(url)
bsObj = BeautifulSoup(request, 'lxml')
content = bsObj.find('div', {'id': 'mw-content-text'}).get_text()
# print(content)
content = bytes(content, 'UTF-8')
# print(content)
content = content.decode('UTF-8')
print(content)
