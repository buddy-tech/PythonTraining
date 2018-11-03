#!/usr/bin/env python3

import re

patt = "(\w+)@"

with open("redata.txt", "r") as file:
    for data in file.readlines():
        url = re.split("::", data)[1]
        loginName = re.match(patt, url).group(1)
        print("Login as:", loginName)
