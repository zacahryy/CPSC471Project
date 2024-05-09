from socket import *
import sys
import os

# Get port num
serverPort = int(sys.argv[1])

# TCP Socket Creation
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)  # Max num of clients
print("Server is ready to receive on port", serverPort)

print("Waiting for connection...")
print("\n")
connectionSocket, addr = serverSocket.accept()
print("Client connected from:", addr)
print("\n")


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
        print("Opening file:", filename)  # Debugging statement
        with open(f"server_files/{filename}", 'rb') as file:  # Open file in binary mode
            data = file.read()
            print("File content:", data)  # Debugging statement
            connectionSocket.sendall(data)
    except FileNotFoundError:
        print("File does not exist")
        connectionSocket.send(b"File not found")


# Function to handle file uploads (PUT command)
def put(filename, connectionSocket):
    try:
        with open(f'server_files/{filename}', "wb") as f:
            while True:
                chunk = connectionSocket.recv(40)
                print(".")
                if not chunk:
                    break
                f.write(chunk)
                break
        connectionSocket.send(b"File uploaded successfully")
        print(f"Received file: {filename}")

    except Exception as e:
        connectionSocket.send(bytes(str(e), encoding='utf8'))


# Function to handle client disconnect and server shutdown (QUIT command)
def quit(connectionSocket, serverSocket):
    connectionSocket.close()
    serverSocket.close()
    print("Server shutting down...")
    sys.exit(0)


# Handle client commands
def handle_client_command(connectionSocket, serverSocket):
    data = connectionSocket.recv(1024).decode()

    print("Received command from client:", data)
    # command, *args = data.split()  # Split the received data into command and arguments
    command = data.split()[0]
    args = [] if len(data)==1 else data.split()[1:]
    # print("args: ")
    # print(args)

    if command == "GET":
        filename = args[0]
        get(filename, connectionSocket)

    elif command == "PUT":
        filename = args[0]
        put(filename,connectionSocket)

    elif command == "ls":
        dir_listing = os.listdir('server_files')
        files_str = "\n".join(dir_listing)
        connectionSocket.send(bytes(str(files_str), encoding='utf8'))
    elif command == "quit":
        quit(connectionSocket, serverSocket)
    else:
        connectionSocket.send(b"Invalid command")



# Inside your while loop where you handle client connections
while 1:
    # Handle client command
    handle_client_command(connectionSocket, serverSocket)
