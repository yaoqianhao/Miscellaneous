import sqlite3

conn = sqlite3.connect("book.db")
print("Opened database successfully")
c = conn.cursor()
c.execute('''CREATE TABLE BOOKINFO
       (ID INT PRIMARY KEY     NOT NULL,
       BOOKNAME           TEXT    NOT NULL,
       AUTHORNAME            TEXT  NOT NULL,
       PRESSNAME           TEXT  NOT NULL,
       STATUS             TEXT  NOT NULL,
       BORROWTIME       INT NOT NULL,
       INSERTTIME       FLOAT  NOT NULL);''')

print("Table created successfully")
conn.commit()
conn.close()