from socket import *
serverName='127.0.0.1'
serverPost=12000
clientSocket=socket(AF_INET,SOCK_DGRAM)
message=input('Input lowercase setence:').encode('ascii')
clientSocket.sendto(message,(serverName,serverPost))
modifiedMessage,serverAddress=clientSocket.recvfrom(2048)
print(modifiedMessage)
clientSocket.close()