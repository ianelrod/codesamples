#!/usr/bin/env python

import subprocess as s
import os
from time import sleep

reg = [ '04', '08', '80' ]
sys = [ '02', '04', '10', '20', '80' ]

for e in range(len(reg)): # a d
    for f in range(len(reg)): # b s
        for g in range(len(sys)): # c read_memory
            sleep(0.1)
            for h in range(len(sys)): # d open

                # convert a, b, c, d to bytes
                a = bytes.fromhex(reg[e])
                b = bytes.fromhex(reg[f])
                c = bytes.fromhex(sys[g])
                d = bytes.fromhex(sys[h])

                shellcode = a + b'\x2f\x10\x10\x80\x10\x10' + a + b'\x20' + a + b'\x66\x10\x10\x81\x10\x10' + a + b'\x20' + a + b'\x6c\x10\x10\x82\x10\x10' + a + b'\x20' + a + b'\x61\x10\x10\x83\x10\x10' + a + b'\x20' + a + b'\x67\x10\x10\x84\x10\x10' + a + b'\x20' + a + b'\x00\x10\x10\x85\x10\x10' + a + b'\x20\x40\x80\x10\x02\x00\x10' + d + a + b'\x40\x02\x00\x10\x02' + b + b'\x04\x10\xff\x10\x40\x00\x10\x40' + a + b'\x04' + c + a + b'\x40\x02\x00\x10\x02' + b +  b'\x04\x10\x00\x10\x10' + a + b'\x04\x40\x01\x10\x08' + a + b'\x40\x40\x00\x10\x01\x00\x40'

                try:
                    p = s.run('/challenge/' + os.getenv('CHALLENGE_NAME'), input=shellcode, capture_output=True, timeout=0.1)
                except s.TimeoutExpired:
                    print('Timeout')
                    continue

                if "pwn.college" in p.stdout.decode('utf-8'):
                    print('Found it!')
                    print(shellcode.hex())
                    print(p.stdout.decode('utf-8'))
                    exit()

