#!/usr/bin/env python3

from socket import *

HOST = "::1"
PORT = 20000
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpClientSocket = socket(AF_INET6, SOCK_DGRAM)

while True:
    data = input("> ")
    if not data:
        break
    data = bytes(data, "utf-8")
    udpClientSocket.sendto(data, ADDR)
    data, addr = udpClientSocket.recvfrom(BUFSIZE)
    if not data:
        break
    print(data.decode("utf-8"))

udpClientSocket.close()
