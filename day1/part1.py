import numpy as np
import os
import pandas
import sys

f = open(sys.argv[1], 'r')
lines = [_.replace('\n', '') for _ in f.readlines()]

depths = np.array(lines, dtype=int)
increases = 0
for i in range(1, len(depths)):
    if depths[i-1] < depths[i]:
        increases += 1

print(increases)