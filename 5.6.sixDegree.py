from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql
import sys

conn = pymysql.connect(host = '127.0.0.1', user = 'root', passwd = 'zhan.0419', db = 'mysql', charset = 'utf8')
cur = conn.cursor()
cur.execute('USE wikipedia')

def insertPageIfNotExists(url):
    sql_select = 'SELECT * FROM pages WHERE url = \'{}\''.format(url)
    try:
        cur.execute(sql_select)
    except:
        print('SQL error: ', sql_select, '\n', sys.exc_info(), sep = '')
        raise

    if cur.rowcount == 0:
        cur.execute('INSERT INTO pages (url) VALUES (\'{}\')'.format(url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]

def insertLink(fromPageId, toPageId):
    sql_select = 'SELECT * FROM links WHERE fromPageId = {} AND toPageId = {}'.format(int(fromPageId), int(toPageId))
    try:
        cur.execute(sql_select)
    except:
        print('SQL error: ', sql_select, '\n', sys.exc_info(), sep = '')
        raise

    if cur.rowcount == 0:
        sql_insert = 'INSERT INTO links (fromPageId, toPageId) VALUES ({}, {})'.format(int(fromPageId), int(toPageId))
        try:
            cur.execute(sql_insert)
        except:
            print(sql_insert, '\n', sys.exc_info(), sep = '')
            raise

        conn.commit()

pages = set()
def getLinks(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 3:
        return;
    pageId = insertPageIfNotExists(pageUrl)
    url = 'http://en.wikipedia.org' + pageUrl
    request = urlopen(url)
    bsObj = BeautifulSoup(request, 'lxml')
    links = bsObj.findAll('a', href = re.compile('^(/wiki/)((?!:).)*$'))
    num = 1
    for link in links:
        if num < 10:
            insertLink(pageId, insertPageIfNotExists(link.attrs['href']))
            if link.attrs['href'] not in pages:
                # We have encountered a new page, add it and search it for links
                newPage = link['href']
                pages.add(newPage)
                print(num, ': ', newPage, sep = '')
                getLinks(newPage, recursionLevel + 1)
            num = num + 1
        else:
            break

getLinks('/wiki/Kevin_Bacon', 0)
cur.close()
conn.close()