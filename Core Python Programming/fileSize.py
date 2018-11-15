#!/usr/bin/env python3

import os
import re
import sys

path = sys.argv[1]
cmd = "ls -lah " + path
dirList = os.popen(cmd, 'r')

def format(size, name):
    print(size+"\t"+name)

for item in dirList:
    dir = re.findall(r'[^\s]+', item)
    if len(dir) == 2:
        format(dir[1], dir[0])
    else:
        format(dir[4], dir[8])
