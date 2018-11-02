#!/usr/bin/env python3

import re

file = open("redata.txt", "r")
patt = "(\w+)@"

for data in file.readlines():
    url = re.split("::", data)[1]
    loginName = re.match(patt, url).group(1)
    print("Login as:", loginName)
