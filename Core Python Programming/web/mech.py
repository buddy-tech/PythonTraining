#!/usr/bin/env python3

"""使用 Mechanize 模拟浏览器"""

from bs4 import BeautifulSoup, SoupStrainer
from mechanicalsoup import StatefulBrowser

br = StatefulBrowser()

# home page
rsp = br.open("http://us.pycon.org/2011/home/")
print("\n***", rsp.url)
print("Confirm home page has 'Log in' link; click it")
page = rsp.text
assert "Log in" in page, "Log in not in page"  # 断言页面有 Log in, 否则退出
rsp = br.follow_link(br.links(link_text="Log in")[0])

# login page
print("\n***", rsp.url)
print("Confirm at least a login form; submit invalid creds")
assert br.select_form(), "no forms on this page"
current_form = br.select_form(nr=0)  # 选择第一个表单
current_form.form["username"] = "xxx"
current_form.form["password"] = "xxx"
rsp = br.submit_selected()

# login page, with error
print("\n***", rsp.url)
print("Error due to invalid creds; resubmit w/valid creds")
assert rsp.url == "https://us.pycon.org/2011/account/login/", rsp.url
page = rsp.text
# 找到登录错误信息
err = str(BeautifulSoup(page, "html.parser").find("h1").string)
print("Login error:", err)

# 下面模拟用正确帐号登录，懒得注册
# assert err == "405 Not Allowed", err
# current_form = br.select_form()
# current_form.form["username"] = YOUR_LOGIN
# current_form.form["password"] = YOUR_PASSWD
# rsp = br.submit_selected()

# # login successful, home page redirect
# print("\n***", rsp.url)
# print("Logged in properly on home page; click Account link")
# assert rsp.url == "https://us.pycon.org/2011/home/", rsp.url
# page = rsp.text
# assert "Logout" in page, "Logout not in page"  # 如果登录成功会有 Logout 字样
# rsp = br.follow_link(br.links(link_text="Account")[0])
#
# # account page
# print("\n***", rsp.url)
# print("Email address parseable on Account page; go back")
# assert rsp.url == "https://us.pycon.org/2011/account/email/", rsp.url
# page = rsp.text
# assert "Email Address" in page, "Missing email addresses"
# mail = str(BeautifulSoup(page, "html.parser").find("table").find("tr").find("td").find("b").string)
# print(f"    Primary e-mail: {mail}")
# rsp = br.back()
