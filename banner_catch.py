import optparse
import socket
import threading
# from scapy.all import *


def scantcp(tgtHost,tgtPort):
    try:
        #建立tcp连接
        connskt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connskt.connect((tgtHost,tgtPort))
        # connskt.send('ViolentPython\r\n')
        results = connskt.recv(2014)
        print('{}/TCP is open'.format(tgtPort))
        # tgtIP = socket.gethostbyname(tgtHost)
        # print(tgtIP)
        print(str(results))
    except:
        print('{}/TCP is closed'.format(tgtPort))
        pass
def portScan(tgtHost,tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except:
        print('Can not resovle {} :Unknow Host'.format(tgtHost))
        return
    try:
        tgtName = socket.gethostbyaddr(tgtHost)
        print('Scan result for {}'.format(tgtName[0]))
    except:
        print('Scan result for '+tgtIP)
    socket.setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('SCan port : {}'.format(tgtPort))
        scantcp(tgtHost,int(tgtPort))
def main():
    parser = optparse.OptionParser('usage %prog -H' + '<target host> -p <target port>')
    parser.add_option('-t', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).strip().split(',')
    portScan(tgtHost,tgtPorts)
if __name__ == '__main__':
    main()