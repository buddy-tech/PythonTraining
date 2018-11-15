#!/usr/bin/env python3

from smtplib import SMTP as smtp
from email.mime.text import MIMEText

from_addr = input("From: ")
password = input("Password: ")
to_addr = input("To: ")
#  smtp_server = input("SMTP server: ")
smtp_server = 'smtp.163.com'
message = MIMEText("Hello, i am an email...", 'plain', 'utf-8')

server = smtp(smtp_server)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], message.as_string())
server.quit()
