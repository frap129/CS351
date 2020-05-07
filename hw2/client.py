#!/usr/bin/python3

import sys
import socket

# Configurables
filePath = "example.txt"
serverIP = "54.235.47.119"

# Argument Parsing
if (len(sys.argv) >= 2):
    filePath = sys.argv[1]
if (len(sys.argv) == 3):
    serverIP = sys.argv[2]

# Constants
serverPort = 351 # CS-351, to be exact
fileSizeLimit = 1024
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
print("Connecting to " + serverIP + ":" + serverPort.__str__())
clientSocket.connect((serverIP, serverPort))
print("Connected!")

# Read File
print("Sending file...")
file = open(filePath, 'rb')
fileBuffer = file.read(fileSizeLimit)

# Send File
clientSocket.send(fileBuffer)
file.close()

# Get Server response
print(clientSocket.recv(fileSizeLimit).decode('utf-8'))

# Close connection
print("Closing connection")
clientSocket.shutdown(socket.SHUT_WR)
clientSocket.close()
