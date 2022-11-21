#!/usr/bin/env python

# this script will emulate the instructions in the emulate.txt file
# and print the output to the screen

# create the registers object
registers = {
    'a': 0x00, # general purpose register
    'b': 0x00, # general purpose register
    'c': 0x00, # general purpose register
    'd': 0x00, # general purpose register
    'i': 0x00, # instruction pointer
    's': 0x00, # stack pointer
    'f': 0x00  # flags
}

# create the stack object
stack = []

# create the memory object
memory = []

# --- Tokenizer ---

ops = ( 'IMM', 'LDM', 'STM', 'WRI', 'STK', 'JMP', 'ADD', 'CMP' )
conds = ( 'NE', 'LG', 'EQ' )
regs = ( 'a', 'b', 'c', 'd', 'i', 's', 'f', )

# A function can be used if there is an associated value
def t_HEX(t):
    r'[0-9a-fA-F]{2}'
    t.value = int(t.value, 16)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])

# --- Parser ---

# IMM
# def p_IMM(t):
    