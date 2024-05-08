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

# Function to handle file downloads (GET command)
def get(filename, connectionSocket):
    try:
        with open(filename, 'rb') as file:
            data = file.read()
            connectionSocket.sendall(data)
    except FileNotFoundError:
        connectionSocket.send(b"File not found")

# Function to handle file uploads (PUT command)
def put(filename, data, connectionSocket):
    try:
        with open(filename, 'wb') as file:
            file.write(data)
            connectionSocket.send(b"File uploaded successfully")
    except Exception as e:
        connectionSocket.send(bytes(str(e), encoding='utf8'))

# Function to handle client disconnect and server shutdown (QUIT command)
def quit(connectionSocket, serverSocket):
    connectionSocket.close()
    serverSocket.close()
    print("Server shutting down...")
    sys.exit(0)
 

# Handle client commands
def handle_client_command(data, connectionSocket, serverSocket):
    if data == "GET":
        filename = data.split()[1]
        get(filename, connectionSocket)
    elif data == "PUT":
        parts = data.split(maxsplit=2)
        filename = parts[1]
        file_data = parts[2].encode('utf-8')
        put(filename, file_data, connectionSocket)
    elif data == "ls":
        #path = os.getcwd()
        dir_listing = os.listdir()
        connectionSocket.send(bytes(str(dir_listing), encoding='utf8'))
    elif data == "quit":
        quit(connectionSocket, serverSocket)
    else:
        connectionSocket.send(b"Invalid command")

# Inside your while loop where you handle client connections
while 1:
    # Accept client connection and receive data
    print("Waiting for connection...")
    print("\n")
    connectionSocket, addr = serverSocket.accept()
    print("Client connected from:",addr)
    print("\n")
    data = connectionSocket.recv(1024).decode()

    # Handle client command
    handle_client_command(data, connectionSocket, serverSocket)


