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

    already_won = np.zeros(len(boards))

    for i in range(len(numbers)-1):
        print('i: ' + str(i))
        for j in range(len(boards)):
            win = winning_board(boards[j], numbers[:i+1])
            if win > 0 and (not already_won[j]):
                # count how many non winners are left. If it's 1, then we're at the end
                count = 0
                for already in already_won:
                    if (not already):
                        count += 1
                if count == 1:
                    print('WINNING SCORE OF {} AT INDEX {}'.format(win*numbers[i], j))

                already_won[j] = True

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
    test_board = test_board.transpose()
    for _ in test_board:
        if sum(_) == 5:
            winning = True

    total_sum = 0
    if winning:
        board = board.transpose()
        for a in range(len(test_board)):
            for b in range(len(test_board[a])):
                if test_board[a][b] == 0:
                    total_sum += board[a][b]

    return total_sum

if __name__ == '__main__':
    main()





