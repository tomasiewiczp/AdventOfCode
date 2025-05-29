# task url: https://adventofcode.com/2021/day/13
import re

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        hashes = [(int(a), int(b))  for line in read_hook.readlines()  if line[0].isdigit() for a,b in [line.strip().split(',')]]
        read_hook.close()
    with open(file_path, "r") as read_hook: 
        instructions = [re.split(r"[ =]",line.strip())[-2:] for line in read_hook.readlines() if line[0].isalpha()]
        return hashes, instructions

def fold(hashes, instruction):
    axis, fold_line = instruction
    moved_points = []
    for x,y in hashes:
        position = int(x) if axis=='x' else int(y)
        new_positions = (2*int(fold_line)-x,y) if axis=='x' else (x,2*int(fold_line)-y)
        if position>int(fold_line):
            moved_points.append(new_positions)
        else:
            moved_points.append((x,y))
    return set(moved_points)


hashes, instructions  = read_input_file('input.txt')
for next_instruction in instructions:
    hashes = fold(hashes, next_instruction)
    break
print(len(hashes))