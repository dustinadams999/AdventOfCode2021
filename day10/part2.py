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
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

incompletes = []

# Find out which lines are incomplete and which are corrupted

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
                        break
                j -= 1
    if not illegal_found:
        incomplete_indexes = [i for i in range(len(temp)) if temp[i] == 1]
        t = []
        i = len(incomplete_indexes) - 1
        #shell()
        while i >= 0:
            t.append(closes[opens.index(line[incomplete_indexes[i]])])
            i -= 1

        incompletes.append(t)

# compute total
scores = []

for incomplete in incompletes:
    t = 0
    for i in incomplete:
        t = (t * 5) + points[i]
    scores.append(t)

scores.sort()

print(scores[len(scores)//2])
