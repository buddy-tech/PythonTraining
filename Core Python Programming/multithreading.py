#!/usr/bin/env python3

import threading
from time import sleep, ctime

loops = [3, 7, 10]

def loop(nloop, nsec):
    print("Start loop", nloop, "at:", ctime())
    sleep(nsec)
    print("Loop", nloop, "done at:", ctime())

def main():
    print("Starting at:", ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print("All done at:", ctime())

if __name__ == '__main__':
    main()

