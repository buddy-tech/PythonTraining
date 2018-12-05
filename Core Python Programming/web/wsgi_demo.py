#!/usr/bin/env python3

"""WSGI 服务器示例（Hello world）"""

from io import StringIO
import os
import sys

def run_wsgi_app(app, environ):
    """WSGI 服务器"""

    body = StringIO()

    def start_response(status, headers):
        body.write("Status: {0}\r\n".format(status))
        for header in headers:
            body.write("{0[0]}: {0[1]}\r\n".format(header))
        return body.write  # 返回 write 函数以便支持遗留服务器(?)

    iterable = app(environ, start_response)
    try:
        if not body.getvalue():  # WSGI 应用没有返回状态信息和头部
            raise RuntimeError("start_response() not called by app!")
        body.write("\r\n{0}\r\n".format("\r\n".join(line for line in iterable)))
    finally:
        if hasattr(iterable, "close") and callable(iterable.close):
            iterable.close()
                   
    sys.stdout.write(body.getvalue())  # 输出 WSGI 应用的返回信息
    sys.stdout.flush()  # 清除缓冲区

def simple_wsgi_app(environ, start_response):
    """WSGI 应用函数"""

    status = "200 OK"
    headers = [("Content-type", "text/plain")]
    start_response(status, headers)

    # 返回可迭代对象，让服务器负责管理数据
    return ["Hello world!"]

if __name__ == "__main__":
    run_wsgi_app(simple_wsgi_app, os.environ)
