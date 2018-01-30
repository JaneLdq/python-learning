from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, 'lxml')

# find the children of the table
# for child in bsObj.find('table', {'id': 'giftList'}).children:
    # print(child)

# find the siblings of the first row
for sibling in bsObj.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)
