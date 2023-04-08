from scapy.all import *
#iptables -A OUTPUT -p tcp --tcp-flags RST RST -s 172.16.44.21 -j DROP
#https://stackoverflow.com/questions/9058052/unwanted-rst-tcp-packet-with-scapy

_port=13337
_server="172.16.44.1"

S = IP(dst=_server)/TCP(dport=_port,flags='S')
ans = sr1(S)
ack = ans[TCP].seq + 1
seq = ans[TCP].ack
A = IP(dst=_server)/TCP(dport=_port,flags='A',ack= ack, seq=seq)
send(A,count=1)
P = IP(dst=_server)/TCP(dport=_port,flags=0x0018, ack=ack, seq=seq)/"hello 1"
size=len("hello 1")
send(P,count=1)
P = IP(dst=_server)/TCP(dport=_port,flags=0x0018, ack=ack, seq=seq+size)/"hello 2"
send(P,count=1)