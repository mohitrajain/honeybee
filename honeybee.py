#!/usr/bin/python
from multiprocessing import Process, Queue
import nmap
import sys
import subprocess
import detect

def execute_out(cmd):
    Command = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    (out, err) = Command.communicate()
    if err:
        logger('Error Executing ' + cmd + ' \n' + err)
    return out

def scanHost(host='127.0.0.1',ports='22,80',arguments='-sV -sS'):
    
    def singleScan(p,ans, ags):
        try:
            nm = nmap.PortScanner()
            a = nm.scan(host,p,arguments=ags)
            ans.put(a)
        except nmap.PortScannerError as err:
            print "Error to connect with " + host + " for port scanning"
            print err
            ans.put('None')

    scanRes = Queue()
    result = []
    for i in ports.split(','):
        p = Process(target=singleScan, args=(i,scanRes,arguments,))
        p.start()
        p.join()
        result.append(scanRes.get())
    '''
    print "----------------------------------------"
    print "HOST "+host+ " All Neccassary Information"
    print "----------------------------------------"
    '''

    for i in range(len(result)):
        tempres = result[i]
        #print tempres
        print "-----------------> PORT "+ ports.split(',')[i]
        
        #print "###############Port "+ports.split(',')[i] +" Open/Closed###########"
        tstate = str(tempres['scan'][host]['tcp'][int(ports.split(',')[i])]['state'])
        #print "TCP Port is "+tstate
        
        
        if tstate == 'open':
            #print "###############Services Running##############"
            service = str(tempres['scan'][host]['tcp'][int(ports.split(',')[i])]['product'])
            print "SERVICE-INFO by TCP:- "+ service
            if ports.split(',')[i] == '22':
                execute_out('./detect.py '+host)
                print "Kippo total honeyscore is "+detect.hs
        
def opscanHost(host='127.0.0.1',arguments='-O'):
    try:
        nmop = nmap.PortScanner()
        return nmop.scan(host,ports=None,arguments=arguments)
    except nmap.PortScannerError as err:
        print "Error to connect with " + host + " for port scanning"
        print err

if len(sys.argv) == 1:
    ores = opscanHost()
    opname = ores['scan']['127.0.0.1']['osmatch'][0]['name']
    #print opname
    scanHost()

if len(sys.argv) == 2:
    ores = opscanHost(sys.argv[1])
    opname = ores['scan'][sys.argv[1]]['osmatch'][0]['name']
    #print opname
    scanHost(sys.argv[1])

if len(sys.argv) == 3:
    ores = opscanHost(sys.argv[1])
    opname = ores['scan'][sys.argv[1]]['osmatch'][0]['name']
    print opname
    if sys.argv[2].find('-') != -1:
        start = int(sys.argv[2].split('-')[0])
        last = int(sys.argv[2].split('-')[1])
        l = [str(i) for i in range(start,last+1)]
        scanHost(sys.argv[1],','.join(l))
    else:
        scanHost(sys.argv[1],sys.argv[2])
    

if len(sys.argv) == 4:
    ores = opscanHost(sys.argv[1])
    opname = ores['scan'][sys.argv[1]]['osmatch'][0]['name']
    #print opname
    scanHost(sys.argv[1],sys.argv[2],sys.argv[3])
