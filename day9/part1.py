import numpy as np
import sys
from IPython import embed as shell

def main():
    f = open(sys.argv[1], 'r')
    lines = [_.replace('\n', '') for _ in f.readlines()]

    grid = np.array([[int(_) for _ in list(line)] for line in lines], dtype=int)

    low_points = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # check the corners
            # check top left corner
            if i == 0 and j == 0:
                if grid[i][j] < grid[i][j+1] and grid[i][j] < grid[i+1][j]:
                    low_points.append(grid[i][j])
            # check top right corner
            elif i == 0 and j == (len(grid[i]) - 1):
                if grid[i][j] < grid[i][j-1] and grid[i][j] < grid[i-1][j]:
                    low_points.append(grid[i][j])
            # check lower right corner
            elif i == (len(grid) - 1) and j == (len(grid[i]) - 1):
                if grid[i][j] < grid[i][j-1] and grid[i][j] < grid[i-1][j]:
                    low_points.append(grid[i][j])
            # check lower left corner
            elif i == (len(grid) - 1) and j == 0:
                if grid[i][j] < grid[i-1][j] and grid[i][j] < grid[i][j+1]:
                    low_points.append(grid[i][j])

            # check the border rows
            # check the top row
            elif i == 0:
                if grid[i][j] < grid[i][j-1] and grid[i][j] < grid[i+1][j] and grid[i][j] < grid[i][j+1]:
                    low_points.append(grid[i][j])
            # check the bottom row
            elif i == (len(grid) - 1):
                if grid[i][j] < grid[i][j-1] and grid[i][j] < grid[i-1][j] and grid[i][j] < grid[i][j+1]:
                    low_points.append(grid[i][j])
            # check the left column
            elif j == 0:
                if grid[i][j] < grid[i-1][j] and grid[i][j] < grid[i][j+1] and grid[i][j] < grid[i+1][j]:
                    low_points.append(grid[i][j])
            # check the right column
            elif j == (len(grid[i]) - 1):
                if grid[i][j] < grid[i-1][j] and grid[i][j] < grid[i][j-1] and grid[i][j] < grid[i+1][j]:
                    low_points.append(grid[i][j])
            # everything else in the middle
            else:
                if grid[i][j] < grid[i][j-1] and grid[i][j] < grid[i+1][j] and grid[i][j] < grid[i][j+1] and grid[i][j] < grid[i-1][j]:
                    low_points.append(grid[i][j])

    low_points = [low + 1 for low in low_points]


    print(sum(low_points))

if __name__ == '__main__':
    main()
