#!/usr/bin/env python3

import re

def findName(str):
    regex = re.compile(r'[A-Z][a-z]+\s[A-Z][a-z]+')
    ans = regex.search(str)
    
    if ans is not None:
        print(ans.group())

findName("Zeng Runquan")
