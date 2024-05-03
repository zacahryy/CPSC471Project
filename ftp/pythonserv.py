#SERVER CODE
from socket import *

#Need to create a get function for serverPort
serverPort = 12000
#data = ''

#TCP Socket Creation
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1) #Max num of clients
print("Server is ready to receive on port " + serverPort)

while 1:
    print("Waiting for connection...")
    connectionSocket, addr=serverSocket.accept()
    print("Client connected from:",addr)
    tmpBuff = 25
    while len(data) != 40:
        tmpBuff = connectionSocket.recv(40)
        if not tmpBuff:
            break
        data += tmpBuff
        #Sending back the received message
        print(data)
        connectionSocket.close()

