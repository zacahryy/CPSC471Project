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
        command = input("ftp > ")
        if(command=="GET"):
            client.send(command.encode())
            break
        else:
            print("Invaid comand")

    #Data buffer
    data = ""
    while True:
        received_data = client.recv(6).decode() #Receive the data sent by the client
        if "<EOF>" in received_data:
            break
        data = data+received_data

    with open(DOWNLOAD_FILE_PATH, "w") as file:
        file.write(data)
        print("Download successful")
    

except Exception as e:
    print("Connection terminated!")
    print(e)

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
