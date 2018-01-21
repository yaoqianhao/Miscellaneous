import sqlite3
str='0000000000'
conn = sqlite3.connect("information.db")
print("Opened database successfully")
c = conn.cursor()
c.execute('''CREATE TABLE DP
       (ID INT PRIMARY KEY     NOT NULL,
       POINTVALUE     TEXT     NOT NULL,
       PATH           TEXT     NOT NULL);''')
c.execute('''CREATE TABLE STATUS
       (ID INT PRIMARY KEY     NOT NULL,
        ST            TEXT     NOT NULL);''')
print("Table created successfully")
c.execute("INSERT INTO STATUS (ID,ST) \
                          VALUES (1,'%s')"%str)
conn.commit()
conn.close()