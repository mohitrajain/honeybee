#!/usr/bin/python
import ftplib
from ftplib import FTP
from sys import argv,exit
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

port=21
usr='anonymous'
pas='123'

def check(cmd):
    global ftp
    print(ftp.sendcmd(cmd))

print(ftp.getwelcome())
ftp.login()
try:
    print(ftp.nlst())
    print(ftp.sendcmd('umask'))
    print(ftp.dir())
    check('idle')
    check('tenex')
    check('open')
except Exception as error:
    print(str(error))

def scan(ip):
    ftp = FTP(ip)

    print(ftp.getwelcome())
    ftp.login()
    try:
        print(ftp.nlst())
        print(ftp.sendcmd('umask'))
        print(ftp.dir())
        check('idle')
        check('open')
        check('tenex')
    except Exception as error:
        if 'implemented' in str(error):
            print 'honeyscore 5: unimplemented commands'

if __name__ == '__main__':
    ip = '127.0.0.1'
    if len(argv) >= 2:
        ip = argv[1]
    if len(argv) >= 3:
        port = int(argv[2])
    if len(argv) >= 4:
        user = argv[3]
    if len(argv) == 5:
        passwd = argv[4]
    if len(argv) < 2:
        print("Usage ftp_client.py <host_address=127.0.0.1> <port_no=21> <username=anonymous> <passwd=123>")
        exit()
    scan(ip)
