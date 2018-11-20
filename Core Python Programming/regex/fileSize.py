#!/usr/bin/env python3

# 输出指定目录下的每个文件的名称及大小

import os
import re
import sys

path = sys.argv[1]
cmd = "ls -lah " + path
dirList = os.popen(cmd, 'r') # 读取命令输出

def format(size, name):
    print(size+"\t"+name)

for item in dirList:
    dir = re.findall(r'[^\s]+', item) # findall返回一个列表

    if len(dir) == 2: # 目录为空
        format(dir[1], dir[0])
    else:
        format(dir[4], dir[8])
