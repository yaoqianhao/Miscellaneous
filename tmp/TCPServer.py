from socket import *
serverPort=13000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(10)
print('The server is ready to receive')
while True:
    connectionSocket,addr=serverSocket.accept()
    print(connectionSocket)
    sentence=connectionSocket.recv(102400)
    if sentence=='dianzi':
        #把垃圾桶信息更新
        connectionSocket.close()
    else if sentence=='shouji':
        #把路径传给手机
        connectionSocket.send(capitalizedSentence)
    connectionSocket.close()
