from itertools import chain
from os import environ

def score(board):
    return min(score_rows(board), score_rows(list(zip(*board))))

def score_rows(board):
    steps = min(max(order.index(num) for num in row) for row in board)
    score = sum(int(num) for num in chain(*board) if order.index(num) > steps) * int(order[steps])
    return steps, score

def getSolutionPart1(boards):
    return min(map(score, boards))

def getSolutionPart2(boards):
    return max(map(score, boards))

if __name__ == "__main__":
    inputFile = open('input.txt', 'r')
    data = open('input.txt').read().splitlines()
    order = data[0].split(',')
    boards = [
        [line.split() for line in board]
        for board in zip(*[data[i::6] for i in range(2, 7)])
    ]
    part = environ.get('part')
    if part == 'part2':
        print(getSolutionPart2(boards))
    else:
        print(getSolutionPart1(boards))
