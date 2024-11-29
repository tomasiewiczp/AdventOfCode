# task url: https://adventofcode.com/2022/day/9
import numpy as np

movements = {
    'R' : (0, 1),
    'L' : (0, -1),
    'U' : (1, 0),
    'D' : (-1, 0)
}

def read_input_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

def find_new_tail_pos(head_pos, tail_pos, movement):
    if abs(head_pos[0]-tail_pos[0]) <= 1 and abs(head_pos[1]-tail_pos[1]) <=1:
        return tail_pos
    horizontal_dist = int(np.sign(head_pos[0] - tail_pos[0]))
    vertical_dist = int(np.sign(head_pos[1] - tail_pos[1]))
    return (tail_pos[0] + horizontal_dist, tail_pos[1] + vertical_dist)

instructions = [line.split() for line in read_input_file("input.txt")]
knots_pos = [[0, 0] for _ in range(10)]
positions = set()

for direction, steps in instructions:
    movement = movements[direction]
    for _ in range(int(steps)):
        knots_pos[0] = [knots_pos[0][0] + movement[0], knots_pos[0][1] + movement[1]]
        for i in range(1, len(knots_pos)):
            knots_pos[i] = find_new_tail_pos(knots_pos[i - 1], knots_pos[i], movement)
        positions.add(knots_pos[9][0] * 1000 + knots_pos[9][1])

print(len(positions))