from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re
import random
import json

def getCountry(ipAddress):
    url = 'http://freegeoip.net/json/' + ipAddress
    try:
        response = urlopen(url).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get('country_code')

def getLinks(articleUrl):
    url = 'https://en.wikipedia.org' + articleUrl
    request = urlopen(url)
    bsObj = BeautifulSoup(request, 'lxml')
    links = bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href = re.compile('^(/wiki/)((?!:).)*$'))
    return links

def getHistoryIPs(pageUrl):
    # Format of version history pages is:
    # http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl = pageUrl.replace('/wiki/', '')
    historyUrl = 'http://en.wikipedia.org/w/index.php?title=' + pageUrl + '&action=history'
    print('history url is: ' + historyUrl)
    request = urlopen(historyUrl)
    bsObj = BeautifulSoup(request, 'lxml')
    # find only the links with class 'mw-anonuserlink' which has IP address
    # instead of usernames
    ipAddresses = bsObj.findAll('a', {'class': 'mw-anonuserlink'})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

links = getLinks('/wiki/Python_(programming_language)')

while(len(links) > 0):
    for link in links:
        print('------------')
        historyIPs = getHistoryIPs(link.attrs['href'])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
            if country is not None:
                print(historyIP + ' is from ' + country)

        newLink =links[random.randint(0, len(links)-1)].attrs['href']
        links = getLinks(newLink)