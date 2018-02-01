import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='mysql')
cur = conn.cursor()
cur.execute("USE scraping")
cur.execute("SELECT * from pages WHERE id=1")
print(cur.fetchone())
cur.close()
conn.close()
