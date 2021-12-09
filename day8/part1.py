import numpy as np
import os
import pandas
import sys

f = open(sys.argv[1], 'r')
lines = [_.replace('\n', '') for _ in f.readlines()]

total = 0
for line in lines:
    for _ in line.split('|')[1].split():
        if len(_) in [2,3,4,7]:
            total += 1

print(total)