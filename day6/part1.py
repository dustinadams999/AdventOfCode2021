import numpy as np
import os
import pandas
import sys

f = open(sys.argv[1], 'r')
days = int(sys.argv[2])
lines = [_.replace('\n', '') for _ in f.readlines()]
f.close()

fishes = np.array(lines[0].split(','), dtype=int)

for i in range(days):
    curr_length = len(fishes)
    print('working on day: {}, size of fishes: {}'.format(i, curr_length))
    for j in range(curr_length):
        if fishes[j] == 0:
            fishes = np.append(fishes, 8)
            fishes[j] = 6
        else:
            fishes[j] -= 1

print(len(fishes))