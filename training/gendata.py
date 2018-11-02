#!/usr/bin/env python3

from random import randrange, choice
from string import ascii_lowercase as lc
from time import ctime

tlds = ('com', 'edu', 'net', 'org', 'gov')

for i in range(randrange(5, 11)):
    dateInt = randrange(2**30)
    dateString = ctime(dateInt)
    loginLen = randrange(4, 8)
    loginName = ''.join(choice(lc) for j in range(loginLen))
    domainLen = randrange(loginLen, 13)
    domain = ''.join(choice(lc) for j in range(domainLen))

    print("%s::%s@%s.%s::%d-%d-%d" % (dateString, loginName, domain, choice(tlds), dateInt, loginLen, domainLen))
