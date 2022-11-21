.intel_syntax noprefix  
.globl _start  
  
.section .text  
  
_start:  
    push 41  
    pop rax  
    push 2  
    pop rdi  
    push 1  
    pop rsi  
    cdq  
    syscall    xchg rdi, rax  
    push rdx  
    mov dx, 0x5000  
    shl rdx, 16  
    xor dl, 0x2  
    push rdx  
    mov rsi, rsp  
    mov al, 49  
    push 16  
    pop rdx  
    syscall  
    xor rdx, rdx  
    xor rsi, rsi  
    mov rax, 50  
    syscall         # SYS_listen  
    xor rdx, rdx  
    xor rsi, rsi  
    mov rdi, 3  
    mov rax, 43  
    syscall         # SYS_accept  
    mov r8, rax  
    xor rdi, rdi  
    mov rax, 57  
    syscall         # SYS_fork  
    cmp rax, 0  
    je x  
    mov rdi, 4  
    mov rax, 3  
    syscall         # SYS_close  
    mov rdi, 0  
    mov rax, 60  
    syscall         # SYS_exit  
    w:  
    sub rsp, 0x300  # child loop  
    mov rdi, 4  
    mov rax, 3  
    syscall         # SYS_close  
    xor rdx, rdx  
    xor rsi, rsi  
    mov rdi, 3  
    mov rax, 43  
    syscall         # SYS_accept  
    mov r8, rax  
    jmp v  
    x:  
    sub rsp, 0x300  # child begin  
    v:  
    xor rdx, rdx  
    xor rsi, rsi  
    lea rsi, [rsp]  
    mov rdx, 4  
    mov rdi, 4  
    mov rax, 0  
    syscall         # SYS_read  
    cmp rsi, 0      # compare for EMPTY  
    je z  
    mov r9, 0x20544547  
    mov rsi, [rsp]  
    cmp rsi, r9     # compare for GET  
    je y  
    mov r9, 0x54534F50  
    mov rsi, [rsp]  
    cmp rsi, r9     # compare for POST  
    jne z  
    xor rdx, rdx    # POST section  
    xor rsi, rsi  
    lea rsi, [rsp+0x8]  
    mov rdx, 17  
    mov rdi, 4  
    mov rax, 0  
    syscall         # SYS_read  
    push rsi  
    lea rsi, [rsp+0x28]  
    mov rdx, 156  
    mov rax, 0  
    syscall         # SYS_read  
    lea rsi, [rsp+0x130]  
    mov rdx, 256  
    mov rax, 0  
    syscall         # SYS_read  
    pop rdi  
    push rax  
    push rsi  
    mov rdx, 0777  
    add rdi, 1  
    mov rsi, 0101  
    mov rax, 2  
    syscall         # SYS_open  
    mov rdx, 100  
    pop rsi  
    pop rdx  
    mov rdi, rax  
    mov rax, 1  
    syscall         # SYS_write  
    mov rax, 3  
    syscall         # SYS_close  
    mov rdi, r8  
    mov rsi, 0x00000000000A0D0A  
    push rsi  
    mov rsi, 0x0D4B4F2030303220  
    push rsi  
    mov rsi, 0x302E312F50545448  
    push rsi  
    mov rsi, rsp  
    mov rdx, 19  
    mov rax, 1  
    syscall         # SYS_write  
    pop r10  
    pop r10  
    pop r10  
    mov rbp, rsp  
    jmp w  
    y:  
    xor rdx, rdx    # GET section  
    xor rsi, rsi  
    lea rsi, [rsp+0x8]  
    mov rdx, 16  
    mov rdi, 4  
    mov rax, 0  
    syscall         # SYS_read  
    push rsi  
    lea rsi, [rsp+0x28]  
    mov rdx, 256  
    mov rax, 0  
    syscall         # SYS_read  
    pop rdi  
    mov rsi, 0  
    mov rax, 2  
    syscall         # SYS_open  
    mov rdx, 256  
    lea rsi, [rsp+0x130]  
    mov rdi, rax  
    mov rax, 0  
    syscall         # SYS_read  
    mov r9, rax  
    mov r10, rsi  
    mov rdi, r8  
    mov rsi, 0x00000000000A0D0A  
    push rsi  
    mov rsi, 0x0D4B4F2030303220  
    push rsi  
    mov rsi, 0x302E312F50545448  
    push rsi  
    mov rsi, rsp  
    mov rdx, 19  
    mov rax, 1  
    syscall         # SYS_write  
    mov rdx, r9  
    mov rsi, r10  
    mov rax, 1  
    syscall         # SYS_write  
    pop r10  
    pop r10  
    pop r10  
    mov rbp, rsp  
    jmp w  
    z:  
    xor rax, rax    # end child  
    xor rdi, rdi  
    xor rsi, rsi  
    xor rdx, rdx  
    mov rdi, 0  
    mov rax, 60  
    syscall         # SYS_exit  
  
  
.section .data