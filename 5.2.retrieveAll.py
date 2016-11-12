import os
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

downloadDir = 'download'
baseUrl = 'http://pythonscraping.com'

def getAbsoluteUrl(baseUrl, source):
    if source.startswith('http://www.'):
        url = 'http://' + source[11:]
    elif source.startswith('http://'):
        url = source
    elif source.startswith('www.'):
        url = source[4:]
        url = 'http://' + source
    else:
        url = baseUrl + '/' + source
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDir):
    path = absoluteUrl.replace('www.', '')
    path = path.replace(baseUrl, '')
    path = downloadDir + path
    dir = os.path.dirname(path)

    if not os.path.exists(dir):
        os.makedirs(dir)

    return path

url = 'http://www.pythonscraping.com'
request = urlopen(url)
bsObj = BeautifulSoup(request, 'lxml')
# downloadList = bsObj.findAll(src = True)
downloadList = bsObj.findAll('img')
# print(downloadList)

for download in downloadList:
    fileUrl = getAbsoluteUrl(baseUrl, download['src'])
    if fileUrl is not None:
        print(fileUrl)
        urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDir))
