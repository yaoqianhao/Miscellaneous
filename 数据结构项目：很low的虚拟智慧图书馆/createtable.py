import sqlite3

conn = sqlite3.connect("login.db")
print("Opened database successfully")
c = conn.cursor()
account='ADMIN'
password='ADMIN'
c.execute('''CREATE TABLE LOGIN
       (ACCOUNT           TEXT    NOT NULL,
       PASSWORD            TEXT  NOT NULL);''')
c.execute("INSERT INTO LOGIN (ACCOUNT,PASSWORD) \
                  VALUES ('%s','%s')"%(account,password));

print("Table created successfully")
conn.commit()
conn.close()