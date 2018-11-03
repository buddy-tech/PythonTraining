#!/usr/bin/env python3

import ftplib
import os
import socket

HOST = "222.200.181.166"
DIRN = "实验1-wifi热点"
FILE = "wifi阅读资料.txt"
username = input("User: ")
password = input("Password: ")

def main():
    try:
        f = ftplib.FTP(HOST)
        f.encoding = 'utf-8'
    except (socket.error, socket.gaierror) as e:
        print("ERROR: cannot reach '%s'" % HOST)
        return
    print("*** Connected to host '%s'" % HOST)

    try:
        f.login(username, password)
    except ftplib.error_perm:
        print("ERROR: cannot login")
        f.quit()
        return
    print("*** Logged in successfully")

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print("ERROR: cannot CD to '%s'" % DIRN)
        f.quit()
        return
    print("*** Changed to '%s' folder" % DIRN)

    try:
        f.retrbinary("RETR %s" % FILE, open(FILE, 'wb').write)
    except ftplib.error_perm:
        print("ERROR: cannot read file '%s'" % FILE)
        os.unlink(FILE)
    else:
        print("*** Downloaded '%s' to CWD" % FILE)
        f.quit()
    
if __name__ == '__main__':
    main()
