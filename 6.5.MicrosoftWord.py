from zipfile import ZipFile
from urllib.request import urlopen
from bs4 import BeautifulSoup
from io import BytesIO

url = 'http://pythonscraping.com/pages/AWordDocument.docx'
request = urlopen(url)
wordFile = request.read()
wordFile = BytesIO(wordFile)
# print(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')
# print(xml_content.decode('utf-8'))

wordObj = BeautifulSoup(xml_content.decode('utf-8'))
textStrings = wordObj.findAll('w:t')
for textElem in textStrings:
    print(textElem.text)