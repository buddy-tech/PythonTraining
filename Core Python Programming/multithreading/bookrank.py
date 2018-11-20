#!python3

"""多线程实现图书排名示例"""
from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib.request import urlopen as uopen
import socket

REGEX = compile(b"#([\d,]+) in Books")  # 编译一个bytes字符串
AMZN = "http://amazon.com/dp/"
ISBNs = {
    "0132269937": "Core Python Programming",
    "0132356139": "Python Web Development with Django",
    "0137143419": "Python Fundamentals",
}

def getRanking(isbn):
    socket.setdefaulttimeout(10)  # 设置socket超时    

    page = uopen("%s%s" % (AMZN, isbn))
    data = page.read()
    page.close()
    return str(REGEX.findall(data)[0], "utf-8")  # 转Unicode字符串

def _showRanking(isbn):
    print("- %r ranked %s" % (ISBNs[isbn], getRanking(isbn)))

def _main():
    print("At", ctime(), "on Amazon...")
    for i in ISBNs:
        # 创建并启动一个线程
        Thread(target=_showRanking, args=(i,)).start()

@register  # 注册一个退出函数
def _atexit():
    print("All done at:", ctime())

if __name__ == "__main__":
    _main()
