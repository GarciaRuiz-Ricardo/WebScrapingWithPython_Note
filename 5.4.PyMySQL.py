import sys
import pymysql

try:
    conn = pymysql.connect(host = '127.0.0.1', user = 'root', passwd = 'zhan.0419', db = 'mysql')
except:
    print('Connection failed: ', sys.exc_info())

if 'conn' in locals():
    cur = conn.cursor()
    cur.execute('USE scraping')
    cur.execute('SELECT * FROM pages WHERE id = 1')
    print(cur.fetchone())
    cur.close()
    conn.close()
