from scapy.all import *
#iptables -A OUTPUT -p tcp --tcp-flags RST RST -s 172.16.44.21 -j DROP
#https://stackoverflow.com/questions/9058052/unwanted-rst-tcp-packet-with-scapy

_port=13337
_server="172.16.44.1"
_payload="hello"
_string = ""

# S = IP( dst=_server)/TCP(dport=_port,flags='S', seq=1)
# send(S, count=1000)

for i in range(0,200):    
    S = IP( dst=_server)/TCP(dport=_port,flags='S', seq=i)
    ans = sr1(S)
    _string += (f'{ans[TCP].flags}, {ans[TCP].seq}, {ans[TCP].ack}, {ans.time}\n')
    
f = open('13337_seq.txt', 'w')
f.write(_string)
