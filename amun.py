#!/usr/bin/python

import kippo
import subprocess
import sys

ip="127.0.0.1"

if len(sys.argv)==2:
    ip=sys.argv[1]

cmd=''

try:
    print('Trying ...')
    cmd=subprocess.check_output("openssl s_client -connect " + ip + ":443", shell=True)
except Exception as e:
    print("Possibly a Honeypot Detected, since the server doesn't has an SSL Certificate!")
    print("HoneyScore: 1")
    sys.exit(0)

# print(type(cmd))

if "dionaea" in str(cmd):
    # print("LOL")
    # print(cmd)
    # print("##############################")
    # print("# Dionaea Honeypot Detected! #")
    # print("##############################")
    print("HoneyScore: 10")

kippo.scan(ip)
print("Kippo Honeyscore is %s ...", kippo.hs['honeyscore'])

# process = subprocess.Popen('openssl s_client -connect ' + ip + ':443', shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=None)
# process.stdin.write('gams "indus89.gms"\r\n')
# o, e = process.communicate()
# print(o)
