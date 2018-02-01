from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd='123456',
                        db='wikipedia', charset='utf8')
cur = conn.cursor()

def insertPageIfNotExists(url):
    cur.execute("SELECT * FROM pages WHERE url = %s", (url))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO pages(url) VALUES (%s)", (url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]

def insertLink(fromId, toId):
    cur.execute("SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s",
                    (int(fromId), int(toId)))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO links(fromPageId, toPageId) VALUES (%s, %s)",
                    (int(fromId), int(toId)))
        conn.commit()

pages = set()
def getLinks(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 4:
        return;
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    for link in bsObj.findAll('a',
                                href=re.compile('^(/wiki/)((?!:).)*$')):
        insertLink(pageId, insertPageIfNotExists(link.attrs['href']))
        if link.attrs['href'] not in pages:
            newPage = link.attrs['href']
            pages.add(newPage)
            getLinks(newPage, recursionLevel+1)

try:
    getLinks("/wiki/Kevin_Bacon", 0)
finally:
    cur.close()
    conn.close()
