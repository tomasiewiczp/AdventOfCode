# task url: https://adventofcode.com/2022/day/8
import bisect
import math 

def read_input_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

def find_first_higher_tree(tree_line, height):
    for i, num in enumerate(tree_line):
        if num >= int(height):
            return i+1
    return i+1

def check_visibility( row_num, column_num ):
    above = [int(row[column_num]) for row in grid[:row_num]]
    above.reverse()
    below = [int(row[column_num]) for row in grid[row_num+1:]]
    left  = [int(value) for value in grid[row_num][:column_num]]
    left.reverse()
    right = [int(value) for value in grid[row_num][column_num+1:]]
    return above,below,left,right

def count_scenic_score(visibility, height):
    return math.prod([find_first_higher_tree(line, height) for line in visibility])

scenic_score = 0
grid = [line.strip() for line in read_input_file("input.txt")]
for row in range(1,len(grid)-1):
    for column in range(1,len(grid)-1):
        visibility = check_visibility(row, column)
        scenic_score = max(scenic_score, count_scenic_score(visibility, grid[row][column]))
print(scenic_score)