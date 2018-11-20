#!python3

"""
信号量示例
一个最大库存为5的糖果机
"""

from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)  # 糖果托盘，此时已有5个糖果可供应

def refill():
    """模仿商家补充糖果"""

    with lock:
        print("Refilling candy...")
        try:
            candytray.release()
        except ValueError:
            print("full, skipping")
        else:
            print("OK")

def buy():
    """
    模仿顾客买糖果
    """

    with lock:
        if candytray.acquire(False):  # 非阻塞标志 False
            print("Buy one")
        else:
            print("empty, skipping")

def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))

def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))

def _main():
    print("starting at:", ctime())
    nloops = randrange(2, 6)
    print("THE CANDY MACHINE (full with %d bars)!" % MAX)
    Thread(target=consumer,
           # 随机给出正偏差，否则库存永远充足
           args=(randrange(nloops, nloops + MAX + 2),)
           ).start()
    Thread(target=producer, args=(nloops,)).start()

@register
def _atexit():
    print("all DONE at:", ctime())

if __name__ == "__main__":
    _main()
