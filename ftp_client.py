#!venv/bin/python
import ftplib
from ftplib import FTP
from sys import argv
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

ip='127.0.0.1'
port=21
usr='anonymous'
pas='123'

if len(argv)>=2:
    ip=argv[1]
if len(argv)>=3:
    port=int(argv[2])
if len(argv)>=4:
    user=argv[3]
if len(argv)==5:
    passwd=argv[4]
if len(argv)<2:
    print("Usage ftp_client.py <host_address=127.0.0.1> <port_no=21> <username=anonymous> <passwd=123>")

ftp = FTP(ip)

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
    check('open')
    check('tenex')
except Exception as error:
    print(str(error))
