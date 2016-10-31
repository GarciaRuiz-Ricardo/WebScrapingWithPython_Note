from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.google.com"
request = urlopen(url)
html = request.read()

bsObj = BeautifulSoup(html)

# get the first occurrence of the tag
print(bsObj.html.body)