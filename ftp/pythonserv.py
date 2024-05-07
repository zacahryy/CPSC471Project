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


while 1:
    print("Waiting for connection...")
    print("\n")
    connectionSocket, addr = serverSocket.accept()
    print("Client connected from:",addr)
    print("\n")

    data = connectionSocket.recv(1024).decode
    elif data == "quit":
        quit()
    elif data =="get":
       get(connectionSocket, data)
    elif data == "put":
        put()
    elif data == "ls":
        listDir()
     conn.sendall(data.encode())

    if(data[0:2] == 'ls'):
        try:
            dirList = os.listdir()
            outputData = "".join([i + "\n" for i in dirList])
            connectionSocket.send(bytes(outputData, encoding='utf8'))
        except Exception as e:
            errorMsg = str(e)
            connectionSocket.send(bytes(errorMsg, encoding='utf8'))
    
        print("working")

# a function that downloads a file or image from server 
# and save it in current directory
def get(connectionSocket,data):
    found = 0
    path = os.getcwd()
    fileName = data[5:]
    print('fileName: '+fileName)
    if 'main' in path:
        print('fileName: '+fileName)
        items = os.scandir()
        for item in items:
            print(item.name)
            if fileName == item.name:
                found = 1
                break
        if found:
            #generate random port number between 3000 & 50000
            portRandom =random.randrange(3000,50000)
            connectionSocket.sendall(str(portRandom).encode())
            dwldSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            dwldSocket.bind(('',portRandom))
            dwldSocket.listen()
            connectionSocket2 , addr = dwldSocket.accept() #Wait for an incoming connection. Return a new socket representing the connection, and the address of the client.
            with open(fileName,'rb') as saveFile:
                connectionSocket2.sendall(saveFile.read())
                saveFile.close()
                connectionSocket2.close()
        else:
            connectionSocket.sendall('Bad Request'.encode())    
        



def listDir():
    with os.scandir() as items:
        res =''
        totalSize=0
        for item in items:
            if item.is_file():
                size = item.stat().st_size
                res += f'{item.name} \t {size}b \n'
                totalSize +=size
            elif item.is_dir():
                res += f'> {item.name} \n'
        res += f'total size: {totalSize}b \n'
        return res



def quit():
    # Send quit conformation
    connectionSocket.send("1")
    # Close and restart the server
  connectionSocket.close()  
    serverSocket.close()
    os.execl(sys.executable, sys.executable, *sys.argv)
        


