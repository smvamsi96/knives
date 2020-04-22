import socket

serverAddress = "127.0.0.1"

serverPort = 5000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((serverAddress, serverPort))

while(True):

    message = clientSocket.recv(1024)
    print(message)
