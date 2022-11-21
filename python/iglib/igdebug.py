#!/usr/bin/env python

from pwn import *

context.terminal = ['tmux', 'splitw', '-p', '80', '-h', '-F' '#{pane_pid}', '-P']

def debug(path):
    with gdb.debug(path, api=True) as p:
        g = p.gdb
        p.sendline(b'512')
        c = cyclic(512)
        p.send(c)
        g.continue_and_wait()
        loc = bytes.fromhex(g.execute('x/ws $rsp', to_string=True).split('\\x')[2].strip()).decode('utf-8')
        stack = g.execute('stack 100', to_string=True)
        offset = cyclic_find(loc) - 1
        log.info('Loc: ' + loc)
        log.info('Offset: ' + str(offset))
        log.info('Stack: \n' + stack)
        return offset

def offset(path):
    with gdb.debug(path, api=True) as p:
        g = p.gdb
        stack = g.execute('stack 250', to_string=True)
        add = g.execute('search aaaa', to_string=True).split('\n')[1]
        bytes.fromhex(add.split('\\x')[2].strip()).decode('utf-8')
        log.info('Stack: \n' + stack)
        log.info('Address: ' + add)