#!/usr/bin/env python3

from socket import *
from time import ctime

HOST = ""
PORT = 20000
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSeverSocket = socket(AF_INET6, SOCK_STREAM)
tcpSeverSocket.bind(ADDR)
tcpSeverSocket.listen(5)

while True:
    print("Waiting for connection...")
    tcpClientSocket, address = tcpSeverSocket.accept()
    print("...connected from:", address)

    while True:
        data = tcpClientSocket.recv(BUFSIZE)
        if not data:
            break
        
        str = "[" + ctime() + "] " + data.decode("utf-8")
        data = bytes(str, "utf-8")
        tcpClientSocket.send(data)

    tcpClientSocket.close()
tcpSeverSocket.close()
