#!/usr/bin/env python

from iglib import *
import pwn
import argparse
import os
import re

parser = argparse.ArgumentParser(description='This is a general CTF script')
parser.add_argument('-n', '--network', dest='network', action='store_true', help="use ssh instead of local")

pwn.context.log_level = 'info'

path = '/challenge/' + os.getenv('CHALLENGE_NAME')
igexam.examine(path)
flag = None
port = 0

# regex
# rdi_r = re.compile(r"rdi = (0x[\d\w]*)")
# chal_r = re.compile(r"[\d(].*$")
# sig_r = re.compile(r"\['(.*)']$")
flag_r = re.compile(r"pwn.college{.*}")

with pwn.process([path], level='info', close_fds=False) if not pwn.args.network else pwn.remote('', port, level='critical') as p:
    # for pwntools: use progress for static steps, status for states, info for notifications

    yan_s = '''
    SYS exit a
    '''

    a = open('0.txt', 'w')
    a.write(yan_s)
    a.close()

    igparse.read_instructions('0.txt', '1.txt')
    igconv.convert('1.txt', '2.txt')

    b = open('2.txt', 'r')
    yan_s = b.read()
    b.close()

    yan_b = bytes.fromhex(yan_s.replace("\\x", ""))

    # exp = asm('''
    # xor rax, rax
    # xor rdi, rdi
    # xor rsi, rsi
    # mov al, 0x5a
    # push rax
    # push rsp
    # pop rdi
    # push 7
    # pop rsi
    # syscall
    # ''')

    # offset = 216

    # add = '00007fffffffe4b0'

    out = p.recvrepeat(1)
    outs = out.decode('utf-8', 'backslashreplace')
    p.info(outs)

    # get dat flag
    p.info("Sending yancode.")
    p.send(yan_b)

    out = p.recvrepeat(1)
    outs = out.decode('utf-8', 'backslashreplace')
    p.info(outs)

    p.wait()

    try:
        flag = igutil.getflag(flag, outs)
    except:
        pass

    try:
        flag = igutil.printflag()
    except:
        pass

    if flag:
        p.success(flag)
    else:
        p.failure("No flag found.")