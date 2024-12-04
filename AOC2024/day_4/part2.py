# task url: https://adventofcode.com/2024/day/3
import re

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

SQUARE_SIZE = 3
squares = [[line[column:column+SQUARE_SIZE] for line in lines[row:row+SQUARE_SIZE]] for row in range(len(lines)-2) for column in range(len(lines[0])-2)]
diagonals = [[''.join([line[i][i] for i in range(SQUARE_SIZE)]), ''.join([line[i][2-i] for i in range(SQUARE_SIZE)])] for line in squares]
print(sum([diagonal[0] in ['MAS', 'SAM'] and diagonal[1] in ['MAS', 'SAM'] for diagonal in diagonals]))