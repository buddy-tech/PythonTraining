#!/usr/bin/env python3

import  threading
from time import sleep, ctime

loops = [2, 4, 7]

class ThreadFunc():
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)  # 将参数以元组形式导入

def loop(nloop, nsec):
    """模仿单个线程"""

    print("Start loop", nloop, "at:", ctime())
    sleep(nsec)  # 模仿线程运行
    print("Loop", nloop, "done at:", ctime())

def main():
    print("Starting at:", ctime())  # 主线程运行
    threads = []
    nloops = range(len(loops))
    
    for i in nloops:
        # 为Thread对象传入可调用对象
        t = threading.Thread(
            target=ThreadFunc(loop,
                              (i, loops[i]),
                              loop.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print("All done at:", ctime())

if __name__ == "__main__":
    main()
