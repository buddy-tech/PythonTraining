#!/usr/bin/env python3

import threading
from time import ctime

class MyThread(threading.Thread):
    def __init__(self, func, args, name):
        threading.Thread.__init__(self)  # 必须先调用父类的构造函数
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.result

    def run(self):
        print("Starting", self.name, "at", ctime())
        self.result = self.func(*self.args)
        print(self.name, "finished at", ctime())
