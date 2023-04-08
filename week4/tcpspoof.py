from scapy.all import *
#iptables -A OUTPUT -p tcp --tcp-flags RST RST -s 172.16.44.21 -j DROP
#https://stackoverflow.com/questions/9058052/unwanted-rst-tcp-packet-with-scapy

_port=80
_server="172.16.44.1"
_payload="hello"


S = IP(dst=_server)/TCP(dport=_port,flags='S')
ans = sr1(S)
ack = ans[TCP].seq + 1
seq = ans[TCP].ack
A = IP(dst=_server)/TCP(dport=_port,flags='A',ack= ack, seq=seq)
send(A,count=1)

P = IP(dst=_server)/TCP(dport=_port,flags=0x0018, ack=ack, seq=seq)/_payload
send(P,count=1)
seq=seq + len(_payload)

P = IP(dst=_server)/TCP(dport=_port,flags=0x0018, ack=ack, seq=seq)/_payload
send(P,count=1)
seq=seq + len(_payload)

P = IP(dst=_server)/TCP(dport=_port,flags=0x0018, ack=ack, seq=seq)/_payload
send(P,count=1)
seq=seq + len(_payload)
