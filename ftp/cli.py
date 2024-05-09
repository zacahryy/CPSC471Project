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

        # Handle server response based on command

        if command.startswith("GET") and not response.startswith(b"File not found"):
            clientSocket.send(command.encode())
            response = clientSocket.recv(1024)
            # print(len(response.decode()))
            if(response.decode()=="File not found"):
                print("FILE DOES NOT EXIST !!!")
            else:
                filename = command.split()[1]
                with open(filename, 'wb') as file:
                    file.write(response)
                    print("+--------- File Content ---------+")
                    print(response.decode())
                    print("+--------------------------------+")
                    print(f"{filename} downloaded successfully")
                    print("+--------------------------------+\n")
        elif command.startswith("PUT"):
            clientSocket.send(command.encode())
            filename = command.split()[1]
            try:
                with open(filename, "rb") as f:
                    while True:
                        chunk = f.read(40)
                        if not chunk:
                            break
                        clientSocket.send(chunk)
                response = clientSocket.recv(1024)
                print("+----------------------------+\n",f"{filename} uploaded successfully\n","+----------------------------+\n")
            except FileNotFoundError:
                print("File does not exist")

        elif command == "ls":
            clientSocket.send(command.encode())
            response = clientSocket.recv(1024)
            print("+------ SERVER FILES ------+")
            files = response.decode().split("\n")
            for file in files:
                print(f" - {file}")
            print("+--------------------------+\n")

        elif command == "quit":
            clientSocket.send(command.encode())
            print("Quitting FTP client")
            break

        else:
            print("ERROR")
            print(response.decode())

    # Close the socket
    clientSocket.close()

if __name__ == "__main__":
    main()