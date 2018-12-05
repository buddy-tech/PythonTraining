#!/usr/bin/env python3

from socket import *

HOST = "localhost"
HOST_V6 = "::1"
PORT = 20000
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpClientSocket = socket(AF_INET, SOCK_STREAM)
tcpClientSocket.connect(ADDR)

while True:
    data = input("> ")
    if not data:
        break
    data = bytes(data, "utf-8")
    tcpClientSocket.send(data)
    data = tcpClientSocket.recv(BUFSIZE)
    if not data:
        break
    print(data.decode("utf-8"))

tcpClientSocket.close()
