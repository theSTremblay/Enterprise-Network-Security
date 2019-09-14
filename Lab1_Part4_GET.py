#!/usr/bin/python
from scapy.all import *
import requests
from matplotlib.pyplot import *
from scapy.utils import RawPcapReader
from scapy.layers.inet import *
import subprocess
import time
# def http_header(packet):
#         http_packet=str(packet)
#         if http_packet.find('GET'):
#                 return GET_print(packet)
#
# def GET_print(packet1):i
#     ret = "***************************************GET PACKET****************************************************\n"
#     ret += "\n".join(packet1.sprintf("{Raw:%Raw.load%}\n").splt(r"\r\n"))
#     ret += "*****************************************************************************************************\n"
#     return ret
#
# sniff(iface='eth0', prn=http_header, filter="tcp port 80")


from scapy.all import *

ip=IP(dst="slashdot.org")
SYN=TCP(sport=1500, dport=80, flags="S", seq=100)
SYNACK=sr1(ip/SYN)

my_ack = SYNACK.seq + 1
ACK=TCP(sport=1050, dport=80, flags="A", seq=101, ack=my+ack)
send(ip/ACK)

payload= '法'
payload2 = '轮'

PUSH=TCP(sport=1050, dport=80, flags="PA", seq=11, ack=my_ack)
send(ip/PUSH/payload)
send(ip/PUSH/payload2)


