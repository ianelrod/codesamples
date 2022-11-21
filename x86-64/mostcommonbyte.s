; most_common_byte(src_addr, size):
;     b = 0
;     i = 0
;     for i <= size-1:
;         b = [src_addr + i]
;         [stack_base - b] += 1
;     b = 0
;     max_freq = 0
;     rax = 0
;     for b <= 0xff:
;         if [stack_base - b] > max_freq:
;             max_freq = [stack_base - b]
;             rax = b
;     return rax

most_common_byte:
    push rbp
    mov rbp, rsp
    sub rsp, 0x1fe
    xor r9, r9
    xor r10, r10
    xor rax, rax
    dec rsi
j:
    cmp r10, rsi
    jg k
    mov r9b, BYTE PTR [rdi + r10]
    mov r11w, WORD PTR [rsp + 0x2*r9]
    inc r11w
    mov WORD PTR [rsp + 0x2*r9], r11w
    inc r10
    jmp j
k:
    xor r9, r9
    xor r10, r10
    xor r11, r11
l:
    cmp r9, 0xff
    jg n
    mov r11w, WORD PTR [rsp + 0x2*r9]
    cmp r11w, r10w
    jle m
    mov r10w, WORD PTR [rsp + 0x2*r9]
    mov al, r9b
m:
    inc r9
    jmp l
n:
    xor r9, r9
    xor r10, r10
    xor r11, r11
    add rsp, 0x1fe
    pop rbp
    ret