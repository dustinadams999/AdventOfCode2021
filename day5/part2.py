import numpy as np
import os
import pandas
import sys
from IPython import embed as shell

f = open(sys.argv[1], 'r')
lines = [_.replace('\n', '') for _ in f.readlines()]

board = np.zeros((1000, 1000), dtype=int)

for line in lines:
    x1 = int(line.split('->')[0].strip().split(',')[0])
    y1 = int(line.split('->')[0].strip().split(',')[1])
    x2 = int(line.split('->')[1].strip().split(',')[0])
    y2 = int(line.split('->')[1].strip().split(',')[1])
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2)+1):
            board[i][x1] += 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2)+1):
            board[y1][i] += 1
    else:
        x_factor = 1
        y_factor = 1
        if x2 < x1:
            x_factor = -1
        if y2 < y1:
            y_factor = -1
        for i in range(abs(x2-x1)+1):
            board[y1+i*y_factor][x1+i*x_factor] += 1

total_count = 0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] > 1:
            total_count += 1

print(total_count)

