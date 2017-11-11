#!/usr/bin/python
import socket
import paramiko
import sys

hs = {'honeyscore':0}

def cipherspecTest(host):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,22))
    t = paramiko.Transport(sock)
    t.start_client()
    #k = t.get_remote_server_key()
    a = t.get_security_options()
    if t.host_key.size == 1024:
       hs['honeyscore']+=2
       print 'honeyscore 2 : diffie-hellman-group-exchange-sha1 used by kippo'

def commandTest(host):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())
    client.connect(host,22,'root','123456')
    try:
        (stdin, stdout, stderr) = client.exec_command('ifconfig')
    except:
        hs['honeyscore']+=3
        print 'honeyscore 3 : commands execution not supported by kippo'

# research by andrew-morris
def andrewMorris(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,22))
    banner = s.recv(1024)
    s.send('\n\n\n\n\n\n\n\n')
    response = s.recv(1024)
    s.close()

    if "168430090" in response:
        hs['honeyscore']+=5
        print 'honeyscore 5 : twisted framework mishandled input '

def scan(host):
    cipherspecTest(host)
    commandTest(host)
    andrewMorris(host)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print '[+] Usage: python %s 1.1.1.1' % sys.argv[0]
        exit()

    host = sys.argv[1]
    cipherspecTest(host)
    commandTest(host)
    andrewMorris(host)
