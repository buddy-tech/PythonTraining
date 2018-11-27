#!/usr/bin/env python3

import requests
from html.parser import HTMLParser
import codecs

fileName = ['xlcteam']

hparse = HTMLParser()
for i in fileName:
    url = "http://cms.nuptzj.cn/about.php?file={0}.php".format(i)
    print("Get file from url:", url)
    localFile = codecs.open(str(i)+'.php', 'w+', 'utf-8')
    result = requests.get(url)
    result.encoding = 'utf-8'
    localFile.write(hparse.unescape(result.text))
