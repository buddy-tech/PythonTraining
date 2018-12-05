#!/usr/bin/env python3

'''Python协程练习'''

import random
import time
import asyncio
import pdb

# yield
def fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        yield b
        a, b = b, a + b
        index += 1
for fib_res in fib(20):
    print(fib_res)

# pdb.set_trace()
# yield/send
def stupid_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_cnt = yield b
        print('let me think {0} secs'.format(sleep_cnt))
        time.sleep(sleep_cnt)
        a, b = b, a + b
        index += 1
print('-'*10 + 'test yield send' + '-'*10)
N = 20
sfib = stupid_fib(N)
fib_res = next(sfib)
while True:
    print(fib_res)
    try:
        fib_res = sfib.send(random.uniform(0, 0.5))
    except StopIteration:
        break

# pdb.set_trace()
# yield from
def copy_fib(n):
    print('I am copy from fib')
    yield from fib(n)  # 迭代完fib生成器才会到下一句
    print('Copy end')
print('-'*10 + 'test yield from' + '-'*10)
for fib_res in copy_fib(20):
    print(fib_res)

# pdb.set_trace()
# yield from/send
def copy_stupid_fib(n):
    print('I am copy from stupid fib')
    yield from stupid_fib(n)
    print('Copy end')
print('-'*10 + 'test yield from and send' + '-'*10)
N = 20
csfib = copy_stupid_fib(N)
fib_res = next(csfib)
while True:
    print(fib_res)
    try:
        fib_res = csfib.send(random.uniform(0, 0.5))
    except StopIteration:
        break

pdb.set_trace()
# asyncio
@asyncio.coroutine
def asy_smart_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = random.uniform(0, 0.2)
        yield from asyncio.sleep(sleep_secs)
        print('Smart one think {0} secs to get {1}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1

@asyncio.coroutine
def asy_stupid_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = random.uniform(0, 0.4)
        # 调用另一个协程，此时线程中断并执行下一个消息循环
        yield from asyncio.sleep(sleep_secs)
        print('Stupid one think {0} secs to get {1}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1

def asy_loop():
    # 获取事件循环
    loop = asyncio.get_event_loop()
    tasks = [
        asyncio.async(asy_smart_fib(10)),
        asyncio.async(asy_stupid_fib(10)),
    ]
    # 执行协程
    loop.run_until_complete(asyncio.wait(tasks))
    print('All fib finished.')
    loop.close()

asy_loop()
