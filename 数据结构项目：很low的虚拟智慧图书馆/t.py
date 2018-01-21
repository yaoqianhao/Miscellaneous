import sqlite3
import time
import random
from xpinyin import Pinyin
p=Pinyin()





print(type(time.time()))
conn = sqlite3.connect("book.db")
c = conn.cursor()
cursor = c.execute("SELECT ID,BOOKNAME,AUTHORNAME,PRESSNAME,STATUS,INSERTTIME FROM BOOKINFO ")
output = []
for row in cursor:
    output.append(row)
print(len(output))
print(output)
#randomized_quick_sort(output,0,len(output)-1,1)
print(output)
conn.close()
