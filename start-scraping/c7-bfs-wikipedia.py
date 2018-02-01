from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connect(host='localhost', user='root',
                passwd='123456', db='wikipedia', charset='utf8')
cur = conn.cursor()

class SolutionFound(RuntimeError):
    def __init__(self, message):
        self.message = message

def getLinks(fromPageId):
    cur.execute("SELECT toPageId FROM links WHERE fromPageId = %s", (fromPageId))
    if cur.rowcount == 0:
        return None
    else:
        return [x[0] for x in cur.fetchall()]

def constructDict(currentPageId):
    links = getLinks(currentPageId)
    if links:
        return dict(zip(links, [{}]*len(links)))
    return {}

def searchDepth(targetPageId, currentPageId, linkTree, depth):
    if depth == 0:
        return linkTree
    if not linkTree:
        linkTree = constructDict(currentPageId)
        if not linkTree:
            return {}
    if targetPageId in linkTree.keys():
        print("TARGET " + str(targetPageId) + " FOUND!")
        raise SolutionFound("PAGE: " + str(currentPageId))

    for k,v in linkTree.items():
        try:
            linkTree[k] = searchDepth(targetPageId, k, v, depth-1)
        except SolutionFound as e:
            print(e.message)
            raise SolutionFound("PAGE: " + str(currentPageId))
    return linkTree

try:
    searchDepth(12170, 1, {}, 4)
    print("No solution found")
except SolutionFound as e:
    print(e.message)
