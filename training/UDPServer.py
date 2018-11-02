#!/usr/bin/env python3

from socket import *
from time import ctime

HOST = ""
PORT = 20000
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpServerSocket = socket(AF_INET6, SOCK_DGRAM)
udpServerSocket.bind(ADDR)

while True:
    print("Waiting for message...")
    data, addr = udpServerSocket.recvfrom(BUFSIZE)
    str = "[" + ctime() + "] " + data.decode("utf-8")
    data = bytes(str, "utf-8")
    udpServerSocket.sendto(data, addr)
    print("...received from and returned to:", addr)

udpSeverSocket.close()
