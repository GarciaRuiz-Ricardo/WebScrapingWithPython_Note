from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):

    try:
        request = urlopen(url)
    except HTTPError as e:
        print('Print error here:\n', e)
        return None

    try:
        html = request.read()
        bsObj = BeautifulSoup(html)
        title = bsObj.head.title
    except AttributeError as e:
        print('Print error here:\n', e)
        return None

    return title


#url = "http://www.baidu.com"
url = "http://www.pythonscraping.com/page/page1.html"
title = getTitle(url)

if title == None:
    print('Title could not be found.')
else:
    print(title)
