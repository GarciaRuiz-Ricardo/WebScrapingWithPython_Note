from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import sys
import datetime
import pymysql

try:
    conn = pymysql.connect(host = '127.0.0.1', user = 'root', passwd = 'zhan.0419', db = 'mysql', charset = 'utf8')
    cur = conn.cursor()
    cur.execute('USE scraping')
except:
    print('Fail to connect to database.\n', sys.exc_info())

random.seed(datetime.datetime.now())

def store(title, content):
    sql = 'INSERT INTO pages (title, content) VALUES (\'{}\', \'{}\')'.format(title, content)
    try:
        cur.execute(sql)
        cur.connection.commit()
    except:
        print(sql)
        print(sys.exc_info())

def getLinks(articleUrl):
    url = 'http://en.wikipedia.org' + articleUrl
    request = urlopen(url)
    bsObj = BeautifulSoup(request, 'lxml')
    title = bsObj.find('h1').get_text()
    content = bsObj.find('div', {'id': 'mw-content-text'}).find('p').get_text()
    store(title, content)
    links = bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href = re.compile('^(/wiki/)((?!:).)*$'))
    return links

links = getLinks('/wiki/Kevin_Bacon')

try:
    num = 0
    while len(links) > 0 and num < 20:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        print(num, ': ', newArticle, sep = '')
        links = getLinks(newArticle)
        num = num + 1
finally:
    cur.close()
    conn.close()
    print('Close connection to database.')