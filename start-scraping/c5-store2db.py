from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
import pymysql

conn = pymysql.connect(host='localhost', user='root',
                        passwd='123456', db='scraping', charset='utf8')
cur = conn.cursor()

random.seed(datetime.datetime.now())

def store(title, content):
    cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\", \"%s\")",
                (title, content))
    cur.connection.commit()

def getLinks(articalUrl):
    html = urlopen("http://en.wikipedia.org" + articalUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    title = bsObj.find('h1').get_text()
    try:
        content = bsObj.find('div', {'id': 'mw-content-text'}).find('p').get_text()
    except AttributeError:
        content = ""
    store(title, content)
    return bsObj.find('div', {'id':'bodyContent'}).findAll('a',
                        href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/kevin_Bacon")
try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()
