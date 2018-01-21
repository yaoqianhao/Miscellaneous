from socket import *
serverName='52.26.109.47'
#serverName='127.0.0.1'
serverPort=13000
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
modifiedSentence=clientSocket.recv(10240)
print('From Server:',modifiedSentence)
sentence=input('Input lowercase sentence:').encode('ascii')
clientSocket.send(sentence)
modifiedSentence=clientSocket.recv(10240)
print('From Server:',modifiedSentence)
clientSocket.close()