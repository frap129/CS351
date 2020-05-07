#!/usr/bin/python3

import socket

# Constants
fileSizeLimit = 1024
serverSocket = socket.socket()
serverPort = 351

# Configurables
serverIP = "172.31.28.97"

# Bind to socket
print("Binding to socket at " + serverIP + ":" + serverPort.__str__())
serverSocket.bind((serverIP, serverPort))
print("Successfully bound to socket")

# Listen for incomming traffic
print("Listening...")
serverSocket.listen(10)

# Receive file
socket, address = serverSocket.accept()
print("Connection from ", address)
file = socket.recv(fileSizeLimit).decode('utf-8')
print("File transfer complete")

lineArr = file.splitlines()
print("Lines:",len(lineArr))
words = 0
chars = 0
for line in lineArr:
    words += len(line.split())
    chars += len(line.strip())
print("Words:", words)
print("Chars:", chars)

socket.send(bytes("Lines: " + len(lineArr).__str__() +
	"\nWords: " + words.__str__() + "\nChars: " + chars.__str__(), 'utf-8'))
