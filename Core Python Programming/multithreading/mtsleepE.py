#!/usr/bin/env python3

from myThread import MyThread
from time import sleep, ctime

loops = [2, 4, 7]

def loop(nloop, nsec):
    """模仿单个线程"""

    sleep(nsec)  # 模仿线程运行

def main():
    print("Starting at:", ctime()) # 主线程运行
    threads = []
    nloops = range(len(loops))
    
    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print("All done at:", ctime())

if __name__ == "__main__":
    main()
