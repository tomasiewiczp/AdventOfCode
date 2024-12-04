# task url: https://adventofcode.com/2024/day/3
import re

def extract_diagonals(matrix):
    main_diagonals = {}
    anti_diagonals = {}
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            main_diagonals.setdefault(row - col, []).append(matrix[row][col])
            anti_diagonals.setdefault(row + col, []).append(matrix[row][col])
    return list(main_diagonals.values())+(list(anti_diagonals.values()))

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

horizontal = [''.join([line[i] for line in lines]) for i in range(len(lines[0]))]
diagonals = [''.join(diagonal) for diagonal in extract_diagonals(lines)]
lines.extend(horizontal)
lines.extend(diagonals)
print(sum([line.count('XMAS') for line in lines])+sum([line.count('SAMX') for line in lines]))