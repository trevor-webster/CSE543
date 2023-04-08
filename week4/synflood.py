from scapy.all import *
#iptables -A OUTPUT -p tcp --tcp-flags RST RST -s 172.16.44.21 -j DROP
#https://stackoverflow.com/questions/9058052/unwanted-rst-tcp-packet-with-scapy

_port=80
ports = [80,13337]
_server="172.16.44.1"
_payload="hello"


for i in range(0,20):    
    dport=ports[i%2]
    S = IP( dst=_server)/TCP(dport=dport,flags='S')
    ans = sr1(S)


