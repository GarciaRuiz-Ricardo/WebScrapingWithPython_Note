from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string

def cleanContent(content):
    content = re.sub('\n+', ' ', content)
    content = re.sub('\[[0-9]*\]', '', content)
    content = re.sub(' +', ' ', content)
    content = bytes(content, 'UTF-8')
    content = content.decode('ascii', 'ignore')
    cleanContent = []
    content = content.split(' ')
    for item in content:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanContent.append(item)
    return cleanContent

def ngrams(content, n):
    content = cleanContent(content)
    output = []
    for i in range(len(content)-n+1):
        output.append(content[i:i+n])
    return output
