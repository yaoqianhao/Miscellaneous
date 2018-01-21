import sqlite3

def mysort(a,num):
    pass


conn = sqlite3.connect("book.db")
c = conn.cursor()
cursor = c.execute("SELECT ID,BOOKNAME,AUTHORNAME,PRESSNAME,STATUS,INSERTTIME FROM BOOKINFO ")
output = []
print(cursor)
mysort(cursor,2)
for row in cursor:
    output.append('%d %s %s %s %s' % (row[0], row[1], row[2], row[3], row[4]))
conn.close()
