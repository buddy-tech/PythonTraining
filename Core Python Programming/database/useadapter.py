#!/usr/bin/env python3

import mysql.connector as mc

USER = input("Username: ")
PASS = input("Password: ")
DBNAME = "test"
NAMELEN = 16
COLSIZ = 10

tformat = lambda s: str(s).title().ljust(COLSIZ)
cformat = lambda s: s.opper().ljust(COLSIZ)

try:
    conn = mc.connect(user=USER, password=PASS, database=DBNAME)
    print("Connected to", DBNAME)

    cursor = conn.cursor()

    print("Creating users table")
    try:
        cursor.execute('''
            CREATE TABLE users(
                login VARCHAR({0}),
                userid INTEGER,
                projid INTEGER)
            '''.format(NAMELEN))
    except mc.OperationalError as err:
        print("Create table filed:", err)

    print("Inserting names into table")
    cursor.execute("INSERT INTO users VALUES('zrquan', 1, 3)")

    cursor.execute("SELECT * FROM users")
    values = cursor.fetchall()
    print("Get values:", values)

    drop = input("Drop the table? (y/n)")
    if drop == "y":
        cursor.execute("DROP TABLE users")
    else:
        pass
except mc.InterfaceError as err:
    print("Connecting failed:", err)
