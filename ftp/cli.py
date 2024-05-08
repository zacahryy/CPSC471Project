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
serverPort = int(sys.argv[2])
file_name = sys.argv[3]

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, int(serverPort)))

while 1:
    cmdInput = input("ftp> ")
    clientSocket.sendall(cmdInput.encode())
    if 
        clientSocket2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        clientSocket2.connect((HOST,int(Data)))
        size_data = receive(clientSocket, 10)  # Receive size of directory listing
        
        # Convert size_data to integer
        size = int(size_data.decode().strip())
        
        # Receive and print the directory listing
        dir_listing = receive(clientSocket, size).decode()
        print(dir_listing)
    elif cmdInput == "quit":
        clientSocket.send(cmdInput.encode())
        break
    else:
        print("Invalid command")

clientSocket.close()
