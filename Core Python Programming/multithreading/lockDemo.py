#!/usr/bin/env python3

from threading import Thread, Lock, currentThread
from time import sleep, ctime
from random import randrange
from atexit import register

class CleanOutputSet(set): # 记录运行中的线程
    def __str__(self):
        return ', '.join(x for x in self)

lock = Lock()
loops = (randrange(2,5) for x in range(randrange(3,7)))
remaining = CleanOutputSet()

def loop(nsec):
    myname = currentThread().name # 记录当前线程名
    with lock: # 使用上下文管理
        remaining.add(myname)
        print('[%s] Started %s' % (ctime(), myname))
    sleep(nsec)
    with lock:
        remaining.remove(myname)
        print('[%s] Completed %s (%d secs)' % (
            ctime(), myname, nsec))
        print('    (remaining: %s)' % (remaining or 'NONE'))

def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()

@register
def _atexit():
    print('all DONE at:', ctime())

if __name__ == '__main__':
    _main()
