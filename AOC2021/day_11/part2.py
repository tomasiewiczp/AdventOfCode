# task url: https://adventofcode.com/2021/day/11
import numpy as np

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return [[int(i) for i in line.strip() ]for line in read_hook.readlines()]

def increase_adjacent(grid, nine_positions):
    nrows, ncols = grid.shape
    new_nine_positions = np.argwhere(grid > 9)
    nine_positions = np.vstack((nine_positions, new_nine_positions))
    if len(nine_positions) == 100:
        return None
    for i, j in new_nine_positions:
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                ni, nj = i + di, j + dj
                if 0 <= ni < nrows and 0 <= nj < ncols and not (di == 0 and dj == 0):
                    grid[ni, nj] += 1
                    
    for i,j in new_nine_positions:
        grid[i, j] = 0 
    if np.argwhere(grid > 9).any():
        return increase_adjacent(grid, nine_positions)
    else:
        for i,j in nine_positions:
            grid[i, j] = 0       
        return grid

lines = np.array(read_input_file('input.txt'))
for i in range(400):
    lines+=1
    lines = increase_adjacent(lines, np.empty((0, 2), dtype=int))
    if lines is None:
        print(i+1)
        break
