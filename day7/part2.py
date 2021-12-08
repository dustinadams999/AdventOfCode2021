import numpy as np
import os
import pandas
import sys

def find_fuel(positions, target):
    total = 0
    for p in positions:
        total += sum(range(1, abs(target - p) + 1))

    return total

f = open(sys.argv[1], 'r')
lines = [_.replace('\n', '') for _ in f.readlines()]

positions = np.array(lines[0].split(','), dtype=int)

start = positions.min()
end = positions.max()

winning = (find_fuel(positions, end), end)

for i in range(start, end+1):
    temp = find_fuel(positions, start+i)
    if temp < winning[0]:
        winning = (temp, start+i)

print(winning)