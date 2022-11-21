#!/usr/bin/env python
from pwn import *
import binwalk

def examine(path):
    # , keyfile='~/.ssh/id_rsa.pub', ignore_config=True
    # s = ssh(host='dojo.pwn.college', user='hacker', ssh_agent=True)
    b = context.binary = ELF(path)

    for module in binwalk.scan(b.path,signature=True,quiet=False,extract=True):
        print ("%s Results:" % module.name)

    for result in module.results:
        print ("\t%s    0x%.8X    %s" % (result.file.name, result.offset, result.description))