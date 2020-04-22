import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverAddress = "127.0.0.1"

serverPort = 6677

serverSocket.bind((serverAddress, serverPort))

serverSocket.listen(5)

while (True):
    clientSocket , addr = serverSocket.accept()
    while (True):
        reMes = str(clientSocket.recv(1024))
        if (reMes != '0'):
            print(f"New Message: {reMes}")
        else:
            print("Connection Closed By Client")
            break
