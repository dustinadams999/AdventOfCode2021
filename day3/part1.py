import numpy as np
import os
import pandas
import sys

f = open(sys.argv[1], 'r')
lines = [_.replace('\n', '') for _ in f.readlines()]

# powers is the leftmost digit is the 0 index
powers = np.array([np.array([a for a in _], dtype=int) for _ in lines], dtype=int).transpose()
occurences = [sum(_) for _ in powers]

gamma_rate_raw = ''.join(['1' if _ > len(lines)//2 else '0' for _ in occurences])
gamma_rate = int(gamma_rate_raw, 2)
epsilon_rate_raw = ''.join(['0' if _ > len(lines)//2 else '1' for _ in occurences])
epsilon_rate = int(epsilon_rate_raw, 2)

print(gamma_rate*epsilon_rate)