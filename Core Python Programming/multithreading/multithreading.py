#!/usr/bin/env python3

import threading
from time import sleep, ctime

loops = [3, 7, 10]

def loop(nloop, nsec):
    """
    模仿单个线程
    """

    print("Start loop", nloop, "at:", ctime())
    sleep(nsec) # 模仿线程运行
    print("Loop", nloop, "done at:", ctime())

def main():
    print("Starting at:", ctime()) # 主线程运行
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops: # wait for all
        threads[i].join() # threads to finish

    print("All done at:", ctime())

if __name__ == '__main__':
    main()

