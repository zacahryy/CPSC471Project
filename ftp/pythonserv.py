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
    elif data =="GET":
       get()
    elif data == "PUT":
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
        


