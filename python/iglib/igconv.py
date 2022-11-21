#!/usr/bin/env python

from .igleg import *

c_1 = get_c1()
c_2 = get_c2()
c_3 = get_c3()

# take a file with hex and convert it to new challenge format
def convert(file0, file1):
    with open(file0, 'r') as f:
        r = f.read()

    r = r.split('\\x')
    r = r[1:]

    # wrap every 3 elements in a list in r
    r = [r[i:i+3] for i in range(0, len(r), 3)]

    # reverse order of 3 strings in each element
    for i in r:
        i.reverse()

    # swap 2nd and 3rd item in each element
    # for i in r:
    #     i[1], i[2] = i[2], i[1]

    # swap 1st and 2nd item in each element
    # for i in r:
    #     i[0], i[1] = i[1], i[0]

    # reverse order of 3 strings in each element
    # for i in r:
    #     i.reverse()

    # use dictionaries to convert each element unless position 0 is 10, in which case use c_3 for position 2 instead of c_2
    for i in r:
        j = i[2]
        k = i[0]
        l = i[1]
        if j in c_1:
            j = c_1[j]
        if j == '01':
            if l in c_2:
                l = c_2[l]
        elif j == '80':
            if l in c_3:
                l = c_3[l]
            if k in c_2:
                k = c_2[k]
        else:
            if k in c_2:
                k = c_2[k]
            if l in c_2:
                l = c_2[l]
        r[r.index(i)] = [k, l, j]

    # combine r elements into one string
    for i in r:
        j = i[0]
        k = i[1]
        l = i[2]
        r[r.index(i)] = j + k + l

    # combine r elements into one string and separate every two characters with "\x"
    r = ''.join(r)
    r = '\\x'.join(r[i:i+2] for i in range(0, len(r), 2))

    # add "\x" to beginning of string
    r = '\\x' + r

    # write string to file
    with open(file1, 'w') as f:
        f.write(r)
