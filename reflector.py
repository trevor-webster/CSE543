#!/usr/bin/env python3
from scapy.all import *



def listen_for_arp(iface, own_ip,own_mac,ip):
    ans = sniff(iface=iface,filter='arp dst host ' + ip, count=1)
    req=ans[0][ARP]
    attacker_ip=req.psrc
    attacker_mac=req.hwsrc
    arp = ARP(hwtype=req.hwtype, op=2, hwsrc=own_mac, psrc=own_ip, hwdst=req.hwsrc, pdst=req.psrc)
    eth=Ether(dst="ff:ff:ff:ff:ff:ff",src=own_mac)
    pkt = eth / arp
    sendp(pkt, return_packets=True)#is-at
    return attacker_ip, attacker_mac


def listen_on_victim(iface,victim_ip, attacker_ip):
    ans = sniff(filter='src host ' + attacker_ip + ' and dst host ' + victim_ip ,count=1,iface=iface)
    payload = ans[0]
    return payload

def send_from_reflector(payload, reflector_ip, attacker_ip, attacker_mac, own_mac, iface):
    #make valid IP packet
    #syntax to get IP packet from Ether
    
    if IP in payload[0]:
        ip = payload[0]
        ip.src=reflector_ip
        ip.dst=attacker_ip

    #eth=Ether(dst=attacker_mac,src=own_mac)
    #pkt=eth/ip
    ans = sr1(ip,iface=iface )
    return ans

def reply_from_victim():
    return

def main():
    if __name__ == '__main__':
        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument('--interface', required=True)
        parser.add_argument('--victim-ip', required=True)
        parser.add_argument('--victim-ethernet', required=True)
        parser.add_argument('--reflector-ip', required=True)
        parser.add_argument('--reflector-ethernet', required=True)
        args=parser.parse_args()
        print(args)
        


    iface=args.interface
    victim_ip=args.victim_ip
    reflector_ip=args.reflector_ip
    own_mac = get_if_hwaddr(iface)
    own_ip=get_if_addr(iface)

    attacker_ip, attacker_mac = listen_for_arp(iface, own_ip,own_mac,args.victim_ip)
    payload = listen_on_victim(iface,victim_ip,attacker_ip)
    send_from_reflector(payload, attacker_mac, own_mac)

    return
    pkt = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="10.0.0.0/24")
    ans, unans = srp(pkt, timeout=2)
    ans.summary(lambda s,r: r.sprintf("%Ether.src% %ARP.psrc%") )

main()