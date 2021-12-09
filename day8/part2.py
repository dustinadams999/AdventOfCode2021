import numpy as np
import os
import pandas
import sys
from IPython import embed as shell

f = open(sys.argv[1], 'r')
lines = [_.replace('\n', '') for _ in f.readlines()]

total = 0
for line in lines:
    codes = {
        '0': '',
        '1': '',
        '2': '',
        '3': '',
        '4': '',
        '5': '',
        '6': '',
        '7': '',
        '8': '',
        '9': ''
    }

    # first figure out the codes
    keys = line.split('|')[0].split()
    keys = sorted(keys, key=lambda x: len(x))
    keys = [''.join(sorted(key)) for key in keys]
    
    vals = line.split('|')[1].split()
    vals = [''.join(sorted(val)) for val in vals]

    # find 1, 4, 7, 8
    codes['1'] = keys[0]
    codes['7'] = keys[1]
    codes['4'] = keys[2]
    codes['8'] = keys[9]

    # next find 0, 6, 9
    for a in keys[6:9]:
        if len(set(list(codes['4'])).intersection(set(list(a)))) == 4:
            codes['9'] = a
        elif len(set(list(codes['7'])).intersection(set(list(a)))) == 2:
            codes['6'] = a
        else:
            codes['0'] = a

    # next find 2, 3, 5
    for a in keys[3:6]:
        if len(set(list(codes['1'])).intersection(set(list(a)))) == 2:
            codes['3'] = a
        elif len(set(list(codes['4'])).intersection(set(list(a)))) == 2:
            codes['2'] = a
        else:
            codes['5'] = a


    true_values = {v: k for k, v in codes.items()}

    sub_total = true_values[vals[0]] + true_values[vals[1]] + true_values[vals[2]] + true_values[vals[3]]

    total += int(sub_total)




print(total)








