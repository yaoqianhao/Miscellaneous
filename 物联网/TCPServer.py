from socket import *
import sqlite3
serverPort=13000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(10)
print('The server is ready to receive')
while True:
    connectionSocket,addr=serverSocket.accept()
    print(connectionSocket)
    sentence=connectionSocket.recv(102400)
    if len(sentence)>=18 and sentence[0]=='T' :
        #把垃圾桶信息更新
        value=0
        for a in range(17,len(sentence)):
            value=value*10+int(sentence[a])
        print(value)
    elif sentence=='shouji' and check1(sentence):
        #把路径传给手机
        conn = sqlite3.connect("information.db")
        print("Opened database successfully")
        c = conn.cursor()
        cursor = c.execute("SELECT ST from STATUS WHERE ID = 1")
        ss=None
        for row in cursor:
            ss=row[0]
        cursor = c.execute("SELECT PATH from DP WHERE POINTVALUE = %s"%ss)
        for row in cursor:
            ss=row[0]
        print(ss)
        conn.commit()
        conn.close()
        connectionSocket.send(ss)
    connectionSocket.close()
