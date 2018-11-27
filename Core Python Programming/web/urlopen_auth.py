#!/usr/bin/env python3

"""基本HTTP验证"""

from urllib import request, error, parse

LOGIN = "zrquan"
PASSWD = "passwd"
URL = "http://localhost"
REALM = "Secure Archive"

def handler_version(url):
    hdlr = request.HTTPBasicAuthHandler()
    hdlr.add_password(REALM, parse.urlparse(url)[1], LOGIN, PASSWD)
    opener = request.build_opener(hdlr)
    # 安装开启器以便所有URL都能使用验证信息
    request.install_opener(opener)
    return url

def request_version(url):
    from base64 import encodestring
    req = request.Request(url)
    b64str = encodestring(bytes(f"{LOGIN}:{PASSWD}", "utf-8"))[:-1]
    req.add_header("Authorization", f"Basic {b64str}")
    return req

for funcType in ("handler", "request"):
    print(f"*** Using {funcType.upper()}")
    url = eval(f"{funcType}_version")(URL)

    with request.urlopen(url) as f:
        print(str(f.readline(), "utf-8"))

