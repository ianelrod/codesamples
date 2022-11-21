#!/usr/bin/env python

from pwn import *
import subprocess as s
import ast
import signal
import os

# b = context.binary = ELF('/challenge/' + os.environ['CHALLENGE_NAME'])
b = context.binary = ELF('/home/hacker/pipe')

port = 0

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
    # so_out = os.open(outpath, os.O_RDONLY | os.O_NONBLOCK)
    # so_in = os.open(outpath, os.O_WRONLY)

# ci = process("cat -", shell=True, stdout=si, close_fds=False)
# co = s.Popen(["rev"], stdout=w, close_fds=False)


with s.Popen('/home/hacker/wrap.sh', text=True, close_fds=False) if not args.REMOTE else remote('', port) as p:
    sleep(1)
    # outs = os.write(r, "asjcescj")
    # w.close()
    # print(outs)
    # pid_r = re.compile(r"\(PID\s(.*)\)")
    # sig_r = re.compile(r"\['.*']$")

    # pid = int(pid_r.search(outs).group(1).strip())
    # sig = sig_r.search(outs).group(0).strip()
    # pid = input("Paste PID here: ")
    # pid = int(pid)
    # sig = input("Paste array here: ")
    # sig = ast.literal_eval(sig)

    # i = 0
    # while i < len(sig):
    #     os.kill(pid, signal.Signals[sig[i]].value)
    #     sleep(0.01)
    #     i+=1