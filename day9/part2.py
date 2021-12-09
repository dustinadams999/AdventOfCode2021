import numpy as np
import sys
from IPython import embed as shell

def main():
    f = open(sys.argv[1], 'r')
    lines = [_.replace('\n', '') for _ in f.readlines()]

    grid = np.array([[int(_) for _ in list(line)] for line in lines], dtype=int)

    reference = np.zeros(grid.shape, dtype=bool)

    basins = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print('working on ({},{})'.format(i,j))
            total = check_basin(reference, grid, i, j)
            basins.append(total)

    basins = [_ for _ in basins if _ != 0]
    basins.sort()
    print(basins[-1]*basins[-2]*basins[-3])

    #shell()

def check_basin(reference, grid, i,j):
    if  i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or reference[i,j] or grid[i][j] == 9:
        return 0
    else:
        reference[i,j] = True
        return 1 + check_basin(reference, grid, i-1, j) + check_basin(reference, grid, i+1, j) + check_basin(reference, grid, i, j-1) + check_basin(reference, grid, i, j+1)

if __name__ == '__main__':
    main()


