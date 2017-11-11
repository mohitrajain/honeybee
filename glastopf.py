#!/usr/bin/python
import requests
import sys
import subprocess

f1='perlshop.cgi'
f2='info.php'
f3='Footer Powered By'
f4='This is a really great entry'

req=""

if len(sys.argv)>=2:
    ip=sys.argv[1]
if len(sys.argv)==3:
    req=sys.argv[2]
if len(sys.argv)<2:
    print('Usage glastopf.py <ip_address>')
    sys.exit(0)

err='.:/usr/share/pear:/usr/share/php'

score=0

r=requests.get('http://' + ip + "?../etc/group")
r=r.text

if 'root' in r or 'daemon' in r or err in r:
    score+=1

r=requests.get('http://' + ip + "?../etc/shadow")
r=r.text

if 'daemon' in r or err in r:
    score+=2


r=requests.get('http://' + ip + "?../etc/passwd")
r=r.text

if 'root' in r or err in r:
    score+=1

r=requests.get('http://' + ip + "/" + req)
r=r.text

if f1 in r or f2 in r or f3 in r or f4 in r or err in r:
    # Is a honeypot most probably ...
    score+=2

print("honeyscore: " + str(score))
