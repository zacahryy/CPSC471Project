#CLIENT CODE
from socket import *
import sys
import os

try:
  serverName = input (" Enter the server name:")
    serverPort = input ("Enter the server port:")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    client.connect((serverNameT, serverPort)) #Connect to the server running on localhost
    
while True:
       

    if 
        clientSocket2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        clientSocket2.connect((serverName,int(Data)))
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
