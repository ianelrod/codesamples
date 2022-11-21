#!/usr/bin/env python3.8

from contextlib import nullcontext
import socketserver
from xml.etree.ElementTree import TreeBuilder
from pwn import *
import subprocess as s
import ast
# import signal
# import os

# b = context.binary = ELF('/challenge/' + os.environ['CHALLENGE_NAME'])
# b = context.binary = ELF('/home/hacker/pipe')

port = 1906
# 254:xsaaenmviu
# x = [""] * 118
# x[0] = b.path
# x[117] = "uptewnkahe"

# y = {"44": "lxmmikmedp"}

inpath = "/tmp/input"
outpath = "/tmp/output"

if os.path.exists(inpath):
    os.unlink(inpath)

if not os.path.exists(inpath):
    os.mkfifo(inpath,mode=0o777)
    si = os.open(inpath,os.O_RDWR)
    # si_out = os.open(inpath,os.O_RDONLY | os.O_NONBLOCK)
    # si_in = os.open(inpath, os.O_WRONLY)

if os.path.exists(outpath):
    os.unlink(outpath)

if not os.path.exists(outpath):
    os.mkfifo(outpath,mode=0o777)
    so = os.open(outpath,os.O_RDWR)
    # so_out = os.open(outpath, os.O_RDONLY | os.O_NONBLOCK)
    # so_in = os.open(outpath, os.O_WRONLY)

# r, w = os.pipe()
# t, x = os.pipe()

# ci = process("/usr/bin/cat", stdout=w, stdin=si, close_fds=False)
# co = process("/usr/bin/cat", stdout=so, stdin=t, close_fds=False)

# stdin=si, stdout=so, 
with s.Popen("cat | /home/hacker/pipe | cat", shell=True, stdin=si, stdout=so, text=True, close_fds=False) if not args.REMOTE else remote('localhost', port) as p:
    # into = os.open(inpath,os.O_WRONLY)
    # outof = os.open(outpath,os.O_RDONLY | os.O_NONBLOCK)
    # sleep(1)
    sleep(0.5)
    # os.write(si, ("riafhnrw\n").encode('utf-8'))
    # outs = p.communicate()[0]
    # outs = p.recv(4096).decode('utf-8')
    outs = os.read(so, 4096).decode('utf-8')
    # outs = os.read(p.stdout.fileno(), 2048).decode('utf-8')
    print(outs)

    flag_r = re.compile(r"pwn.college{.*}")
    # pid_r = re.compile(r"\(PID\s(.*)\)")
    chal_r = re.compile(r"[\d(].*$")
    # sig_r = re.compile(r"\['.*']$")
    flag = None

    # pid = int(pid_r.search(outs).group(1).strip())
    # sig = sig_r.search(outs).group(0).strip()
    # pid = input("Paste PID here: ")
    # pid = int(pid)
    # sig = input("Paste array here: ")
    # sig = ast.literal_eval(sig)

    try:
        flag = flag_r.search(outs).group(0).strip()
        print("[FLAG] " + flag)
    except:
        pass

    # i = 0
    while not flag:
        chal = chal_r.search(outs).group(0).strip()
        print("Problem: " + chal)
        sol = str(eval(chal))
        print("Solution: " + sol)
        # os.kill(pid, signal.Signals[sig[i]].value)
        os.write(si, (sol + "\n").encode('utf-8'))
        # p.sendline((sol).encode('utf-8'))
        sleep(.01)

        # outs = p.recv(2048).decode('utf-8')
        outs = os.read(so, 4096).decode('utf-8')
        # outs = os.read(p.stdout.fileno(), 256).decode('utf-8')
        print(outs)

        try:
            flag = flag_r.search(outs).group(0).strip()
            print("[FLAG] " + flag)
        except:
            pass
        # i+=1

    # base = 0x0000555555555555
    # offset = 24
    # Send the payload
    # x = flat({offset: base - 0x033C})
    # p.sendline(x)

    # if flag:
    #     p.success(flag)
    # else:
    #     p.failure(outs)