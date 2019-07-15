import optparse
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *


parser = optparse.OptionParser()
parser.add_option('-t', dest="tgt host", type='string')
(options,args)=parser.parse_args()
tgt_host = options.tgthost
tgt_host = str(tgt_host).strip()
prefix = tgt_host.split('.')[0]+'.'+tgt_host.split('.')[1]+'.'+tgt_host.split('.')[2]+'.'


for address in range(254):
    answer = sr1(ARP(pdst=prefix+str(address)), timeout=0.1, verbose=0)
    if answer:
        print(prefix + str(address))
    else:
        pass

