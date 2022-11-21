#!/usr/bin/env python
from pwn import *

def mkpipe(path):
    if os.path.exists(path):
        os.unlink(path)
    if not os.path.exists(path):
        os.mkfifo(path,mode=0o777)
        pipe = os.open(path,os.O_RDWR)
        # p_o = os.open(inpath,os.O_RDONLY | os.O_NONBLOCK)
        # p_i = os.open(inpath, os.O_WRONLY)
    return pipe

def printflag():
    flag = os.open('/flag', os.O_RDONLY)
    flag = os.read(flag, 0x100).decode('utf-8')
    return flag

def getflag(outs, flag_r):
    flag = flag_r.search(outs).group(0).strip()
    return flag