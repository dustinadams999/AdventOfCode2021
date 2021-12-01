import numpy as np
import os
import pandas
import sys

f = open(sys.argv[1], 'r')
lines = [_.replace('\n', '') for _ in f.readlines()]

depths = np.array(lines, dtype=int)
increases = 0
for i in range(3, len(depths)):
    if (depths[i-1] + depths[i-2] + depths[i-3]) < (depths[i] + depths[i-1] + depths[i-2]):
        increases += 1

print(increases)