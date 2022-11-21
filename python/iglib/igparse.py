#!/usr/bin/env python

from .igleg import *

b_1 = get_b1()
b_2 = get_b2()
b_3 = get_b3()

# take a file with hex and convert it to yan85 assembly
def read_hex(file0, file1):
    with open(file0, 'r') as f:
        r = f.read()

    r = r.strip()
    r = r.split('\n')
    r = r[:-1]

    # remove leading whitespace from each element
    for i in r:
        j = i.lstrip(' ')
        r[r.index(i)] = j

    for i in r:
        j = i.replace('0x', '')
        r[r.index(i)] = j
        if len(j) == 15:
            r[r.index(j)] = '0' + j

    # convert each qword into a byte array and reverse it
    for i in r:
        j = bytearray.fromhex(i)
        j.reverse()
        r[r.index(i)] = j

    # combine r into one byte string and make new list with 3 bytes per element
    r = b''.join(r)
    r = [r[i:i+3] for i in range(0, len(r), 3)]

    # convert each element into hex string
    for i in r:
        j = i.hex()
        r[r.index(i)] = j

    # reverse order of 3 bytes in each element
    for i in r:
        j = i[4:6] + i[2:4] + i[0:2]
        r[r.index(i)] = j

    # swap 2nd and 3rd byte in each element
    for i in r:
        j = i[0:2] + i[4:6] + i[2:4]
        r[r.index(i)] = j

    # parse r using dictionary keys
    for i in r:
        j = i[0:2]
        k = i[2:4]
        l = i[4:6]
        if j in b_1:
            j = b_1[j]
        if j == 'SYS':
            if k in b_3:
                k = b_3[k]
        elif j != 'JMP':
            if k in b_2:
                k = b_2[k]
        # if j == 'JMP' and l in cond_dict:
        #     l = cond_dict[l]
        if j != 'IMM' and l in b_2:
            l = b_2[l]
        if j == 'STM':
            k = '*' + k
        m = ' '.join([j, k, l])
        r[r.index(i)] = m

    # print each element of r and write to emulate.txt
    with open(file1, 'w') as f:
        for i in r:
            f.write(i + '\n')

# take a file with yan85 assembly and convert it to hex
def read_instructions(file0, file1):
    with open(file0, 'r') as f:
        r = f.read()

    r = r.strip()
    r = r.split('\n')

    # remove leading whitespace from each element
    for i in r:
        j = i.lstrip(' ')
        r[r.index(i)] = j

    # separate each element into 3 parts
    for i in r:
        j = i.split(' ')
        r[r.index(i)] = j

    # if 2nd or 3rd element in each sublist is 0, make it 00
    for i in r:
        if i[2] == '0':
            i[2] = '00'
        if i[1] == '0':
            i[1] = '00'

    # remove * from 2nd element if it exists
    for i in r:
        if i[1][0] == '*':
            j = i[1][1:]
            i[1] = j

    # convert values into keys
    for i in r:
        j = i[0]
        k = i[1]
        l = i[2]
        # if j == 'JMP':
        #     for key, value in cond_dict.items():
        #         if l == value:
        #             l = key
        if j == 'SYS':
            for key, value in b_3.items():
                if k == value:
                    k = key
            for key,value in b_2.items():
                if l == value:
                    l = key
        else:
            for key, value in b_2.items():
                if k == value:
                    k = key
                if l == value:
                    l = key
        for key, value in b_1.items():
            if j == value:
                j = key
        m = ''.join([j, k, l])
        r[r.index(i)] = m

    # check if each element is 6 bytes long
    for i in r:
        if len(i) != 6:
            raise Exception(i + ' is not 6 bytes long')

    # prepend \x to each element in r sublists
    for i in r:
        j = i[0:2]
        k = i[2:4]
        l = i[4:6]
        j = '\\x' + j
        k = '\\x' + k
        l = '\\x' + l
        m = ''.join([k, l, j])
        r[r.index(i)] = m

    # create one string from r
    r = ''.join(r)

    # convert string into byte string
    # r = bytes.fromhex(r)

    # write string to file
    with open(file1, 'w') as f:
        f.write(r)
