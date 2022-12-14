#!/usr/bin/env python

# standard:
# op des src
# op call reg

# old:
# des src op
# call reg op

# new:
# src des op
# reg call op

# op
b_1 = {
    '01': 'CMP', # 10 -> 10
    '02': 'IMM', # 04 -> 01
    '04': 'ADD', # 01 -> 04
    '08': 'JMP', # 02 -> 20
    '10': 'LDM', # 40 -> 40
    '20': 'SYS', # 80 -> 80
    '40': 'STK', # 08 -> 02
    '80': 'STM'  # 20 -> 08
}

# reg
b_2 = {
    '01': 'c', # 04 -> 40
    '02': 'd', # 20 -> 08
    '04': 'b', # 10 -> 20
    '08': 'a', # 02 -> 01
    '10': 'i', # 01 -> 04
    '20': 'f', # 08 -> 02
    '40': 's'  # 40 -> 10
}

# sys
b_3 = {
    '01': 'read_code', # 04
    '02': 'read_memory', # 01
    '04': 'write', # 10
    '08': 'sleep', # 20
    '10': 'exit', # 02
    '20': 'open' # 08
}

# op
c_1 = {
    '01': '10',
    '02': '01',
    '04': '04',
    '08': '20',
    '10': '40',
    '20': '80',
    '40': '02',
    '80': '08'
}

# reg
c_2 = {
    '01': '40',
    '02': '08',
    '04': '20',
    '08': '01',
    '10': '04',
    '20': '02',
    '40': '10'
}

# sys
c_3 = {
    '01': '04',
    '02': '01',
    '04': '10',
    '08': '20',
    '10': '02',
    '20': '08'
}

def get_c1():
    return c_1

def get_c2():
    return c_2

def get_c3():
    return c_3

def get_b1():
    return b_1

def get_b2():
    return b_2

def get_b3():
    return b_3

# cond_dict = {
#     '04': 'EQ',
#     '09': 'LG',
#     '10': 'NE'
# }