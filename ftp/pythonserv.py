#SERVER CODE
from socket import *
import sys
import os

#Get port num
serverPort = int(sys.argv[1])


#TCP Socket Creation
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1) #Max num of clients
print("Server is ready to receive on port", serverPort)

def receive(socket, numBytes):
    data = ''
    tmpBuff = ''

    while len(data) < numBytes:
        tmpBuff = socket.recv(numBytes)

        if not tmpBuff:
            break

        data += tmpBuff

    return data


while 1:
    print("Waiting for connection...")
    print("\n")
    connectionSocket, addr = serverSocket.accept()
    print("Client connected from:",addr)
    print("\n")

    data = connectionSocket.recv(1024).decode()

    if(data[0:2] == 'ls'):
        try:
            dirList = os.listdir()
            outputData = "".join([i + "\n" for i in dirList])
            connectionSocket.send(bytes(outputData))
        except Exception as e:
            errorMsg = str(e)
            connectionSocket.send(bytes(errorMsg))
    
        print("working")






        
connectionSocket.close()

