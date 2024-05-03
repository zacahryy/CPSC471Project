#CLIENT CODE
from socket import *

#Name and port number of server
#Need to write a get function for server name and port
serverName = ecs.fullerton.edu
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)

data = "Hello World!"

while bytesSent != len(data):
    bytesSent = clientSocket.send(data[bytesSent:])
    clientSocket.close()