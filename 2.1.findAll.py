from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/warandpeace.html"
request = urlopen(url)
bsObj = BeautifulSoup(request)

nameList = bsObj.findAll('span', {'class':'green'})
for name in nameList:
    print(name.get_text())

textList = bsObj.findAll(text='the prince')
print(len(textList))

allText = bsObj.findAll(id='text')
print(allText[0].get_text())


# bsObj.findAll('', {'id':'text'})
# bsObj.findAll(class_='green')
# bsObj.findAll('', {'class':'green'})

# findAll find all the tags, find find the first tag

