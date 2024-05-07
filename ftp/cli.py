#CLIENT CODE
from socket import *
import sys
import os

#Name and port number of server
#Need to write a get function for server name and port
def receive(socket, numBytes):
    data = ''
    tmpBuff = ''

    while len(data) < numBytes:
        tmpBuff = socket.recv(numBytes)

        if not tmpBuff:
            break

        data += str(tmpBuff)

    return data

serverName = sys.argv[1]
serverPort = sys.argv[2]

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, int(serverPort)))

while 1:
    cmdInput = input("ftp> ")

    if(cmdInput[0:2] == 'ls'):
        clientSocket.send('ls'.encode())

        size = receive(clientSocket, 10)

        #error testing
        print(size)
        print(type(size))
        print(size.encode())
        print(int.from_bytes(size.encode(), "big"))

        #line with error
        print(receive(clientSocket, int.from_bytes(size.encode(), "big")))

    data = clientSocket.recv(1024).decode()
clientSocket.close()
