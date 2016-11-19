from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator

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
    output = {}
    for i in range(len(content)-n+1):
        ngramTemp = ' '.join(content[i:i+n])
        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output

content = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read(), 'utf-8')
ngrams = ngrams(content, 2)
sortedNGrams = sorted(ngrams.items(), key = operator.itemgetter(1), reverse = True)
print(sortedNGrams)