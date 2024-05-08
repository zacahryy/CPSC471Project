from socket import *
import sys
import os

# Name and port number of server
def receive(socket, numBytes):
    data = ''
    tmpBuff = ''

    while len(data) < numBytes:
        tmpBuff = socket.recv(numBytes)

        if not tmpBuff:
            break

        data += str(tmpBuff)

    return data

if len(sys.argv) < 4:
    print("Usage: python cli.py <server_name> <server_port> <filename>")
    sys.exit(1)

serverName = sys.argv[1]
serverPort = int(sys.argv[2])
file_name = sys.argv[3]

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    command = input('ftp> (e.g., GET filename, PUT filename, ls, quit): ')
    if command.lower() == 'quit':
        clientSocket.sendall(command.encode())
        break

    # You need to define download_file function or remove this call if not needed
    # download_file(clientSocket, command)

while True:
    # Add condition for the second while loop
    if True: 
        clientSocket2 = socket(AF_INET, SOCK_STREAM)
        clientSocket2.connect((serverName, serverPort))
        size_data = receive(clientSocket, 10)  # Receive size of directory listing
        
        # Convert size_data to integer
        size = int(size_data.strip())
        
        # Receive and print the directory listing
        dir_listing = receive(clientSocket, size)
        print(dir_listing)
    else:
        cmdInput = input("Enter command: ")
        if cmdInput == "quit":
            clientSocket.send(cmdInput.encode())
            break
        else:
            print("Invalid command")

clientSocket.close()