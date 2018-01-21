from socket import *

HOST = '127.0.0.1'
PORT = 8083
BUFSIZE = 65535
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

welcomeStr = 'Welcome to 12.1 python socket server'


def logFileRead(logFile):
    '''
    Read logFile by line
    return List
    '''
    logFileDealList = []
    with open(logFile, 'r') as logFileContent:
        for line in logFileContent.readlines():
            logFileDealList.append(line)
    return logFileDealList


if __name__ == "__main__":
    fileDir = 'filePath/warningMessage.txt'

    while True:
        print
        'Enter 12.1 python socket server'
        tcpCliSock, addr = tcpSerSock.accept()
        print
        'Connected from : ', addr
        data = tcpCliSock.recv(BUFSIZE)

        if not data:
            break
        print
        data
        logFileContentList = logFileRead(fileDir)
        # print logFileContentList
        for fileContent in logFileContentList:
            if fileContent.find('pending') == -1:
                continue
            tcpCliSock.send('%s' % fileContent)
        tcpCliSock.close()

    tcpSerSock.close()
