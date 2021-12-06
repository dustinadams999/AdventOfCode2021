import numpy as np
import os
import pandas
import sys
from IPython import embed as shell


f = open(sys.argv[1], 'r')
lines = [_.replace('\n', '') for _ in f.readlines()]

powers = np.array([np.array([a for a in _], dtype=int) for _ in lines], dtype=int).transpose()

length = len(lines[0])

oxygen_lines = lines
carbon_lines = lines

for a in range(length):
    # first go through and find how many occurences of that bit
    oxygen_ones_occurences = sum([int(_[a]) for _ in oxygen_lines])
    oxygen_criteria = '1' if oxygen_ones_occurences >= len(oxygen_lines)/2 else '0'

    # then go through and remove all lines that don't fit the criteria
    if len(oxygen_lines) != 1:
        new_oxygen_list = []
        for oxygen_line in oxygen_lines:
            if oxygen_line[a] == oxygen_criteria:
                new_oxygen_list.append(oxygen_line)

        oxygen_lines = new_oxygen_list


    carbon_ones_occurences = sum([int(_[a]) for _ in carbon_lines])
    carbon_criteria = '0' if carbon_ones_occurences >= len(carbon_lines)/2 else '1'

    # then go through and remove all lines that don't fit the criteria
    if len(carbon_lines) != 1:
        new_carbon_list = []
        for carbon_line in carbon_lines:
            if carbon_line[a] == carbon_criteria:
                new_carbon_list.append(carbon_line)

        carbon_lines = new_carbon_list

print(int(oxygen_lines[0], 2) * int(carbon_lines[0], 2))