from socket import *

def main():
    # Server details
    serverName = 'localhost'
    serverPort = int(input("Enter server port: "))

    # Create socket
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    while True:
        # Get user command
        command = input("ftp> ")

        # Send command to server
        clientSocket.send(command.encode())

        # Receive response from server
        response = clientSocket.recv(1024)

        # Handle server response based on command
        if command.startswith("GET ") and not response.startswith(b"File not found"):
            filename = command.split()[1]
            with open(filename, 'wb') as file:
                file.write(response)
                print("File", filename, "downloaded successfully")
        elif command.startswith("PUT ") and response.startswith(b"File uploaded successfully"):
            print("File uploaded successfully")
        elif command == "ls":
            print(response.decode())
        elif command == "quit":
            print("Quitting FTP client")
            break
        else:
            print(response.decode())

    # Close the socket
    clientSocket.close()

if __name__ == "__main__":
    main()
