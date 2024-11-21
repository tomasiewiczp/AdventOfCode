# task url: https://adventofcode.com/2022/day/8

def read_input_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

def check_visibility(height, row_num, column_num ):
    above = max([int(row[column_num]) for row in grid[:row_num]])
    below = max([int(row[column_num]) for row in grid[row_num+1:]])
    left  = max([int(value) for value in grid[row_num][:column_num]])
    right = max([int(value) for value in grid[row_num][column_num+1:]])
    return all(height <= value for value in [above, below, left, right])

grid = [line.strip() for line in read_input_file("input.txt")]
visible_trees = 4*len(grid)-4 #the outer grid
for row in range(1,len(grid)-1):
    for column in range(1,len(grid)-1):
        if not check_visibility(int(grid[row][column]), row,column ):
            visible_trees+=1
print(visible_trees)