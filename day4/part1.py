import numpy as np
import os
import pandas
import sys
from IPython import embed as shell

def main():
    f = open(sys.argv[1], 'r')
    lines = [_.replace('\n', '') for _ in f.readlines()]

    numbers = np.array(lines[0].split(','), dtype=int)

    boards = []

    line = 2
    while line < len(lines):
        board = []
        for i in range(5):
            board.append(lines[line].split())
            line += 1

        line += 1
        boards.append(board)

    boards = np.array(boards, dtype=int)

    for i in range(len(numbers)):
        print('i: ' + str(i))
        scores = []
        for j in range(len(boards)):
            scores.append(winning_board(boards[j], numbers[:i]))

        for j in range(len(scores)):
            if scores[j] > 0:
                print('WINNING SCORE OF: {}'.format(scores[j]*numbers[i-1]))
                exit()

def winning_board(board, numbers):
    test_board = np.zeros((5,5), dtype=int)

    for number in numbers:
        for a in range(len(board)):
            for b in range(len(board[a])):
                if board[a][b] == number:
                    test_board[a][b] = 1

    winning = False
    # first try horizontal
    for _ in test_board:
        if sum(_) == 5:
            winning = True

    # now try vertical
    test_board.transpose()
    for _ in test_board:
        if sum(_) == 5:
            winning = True

    total_sum = 0
    if winning:
        for a in range(len(test_board)):
            for b in range(len(test_board[a])):
                if test_board[a][b] == 0:
                    total_sum += board[a][b]

    return total_sum

if __name__ == '__main__':
    main()





