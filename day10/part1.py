import numpy as np
import sys
from IPython import embed as shell

f = open(sys.argv[1], 'r')
lines = [_.replace('\n', '') for _ in f.readlines()]

opens = [
    '(',
    '{',
    '[',
    '<'
]

closes = [
    ')',
    '}',
    ']',
    '>'
]

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

illegals = []

for line in lines:
    temp = np.zeros(len(line), dtype=int)
    illegal_found = False
    for i in range(len(line)):
        if illegal_found:
            break
        if line[i] in opens:
            temp[i] = 1
        else:
            # start walking backwards and see if the most recent open is the appropriate open
            j = i - 1
            while j >= 0:
                if temp[j] == 1:
                    if opens.index(line[j]) == closes.index(line[i]):
                        temp[i] = 2
                        temp[j] = 2
                        break
                    else:
                        illegal_found = True
                        illegals.append(line[i])
                        break
                j -= 1

# now compute points
total_sum = 0
for illegal in illegals:
    total_sum += points[illegal]

print(total_sum)


