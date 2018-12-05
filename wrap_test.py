#!/usr/bin/env python3

"""装饰器原理"""

import time
from functools import wraps
import pdb

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n):
    while n > 0:
        n -= 1

if __name__ == "__main__":
    pdb.set_trace()
    countdown(100)
