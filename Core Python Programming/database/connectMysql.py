#!/usr/bin/env python3

import mysql.connector as mc

user = input("Username: ")
password = input("Password: ")
database = 'StudentScore'

conn = mc.connect(user=user, password=password, database=database)
cursor = conn.cursor()

cursor.execute("select CName from Course where credit > 3")
values = cursor.fetchall()
print(values)
