# task url: https://adventofcode.com/2022/day/4
import re
from collections import deque

def read_input_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

def split_stacks_and_instructions(file_path):
    stack = []
    instructions = []
    instruction_part = False
    for line in read_input_file(file_path):
        match line:
            case line if line.startswith('['):
                stack.append(line)
            case line if line.startswith('move'):
                instructions.append(line.strip())
            case '':
                continue
    return stack,instructions

def create_stacks(stack):
    stacks_amount = len(stack[0]) // 4
    stc = {num: deque() for num in range(stacks_amount)}
    
    for line in stack[:-1]:
        for num in range(stacks_amount):
            item = line[1 + 4 * num]
            if item != ' ':
                stc[num].appendleft(item)
    return stc

def make_a_move(stacks, instruction):
    items = []
    for move in range(instruction[0]):
        items.append(stacks[instruction[1]-1].pop())
    for item in items[::-1]:
        stacks[instruction[2]-1].append(item)      
    return stacks

stack,instructions = split_stacks_and_instructions('input.txt')
stacks_dict = create_stacks(stack)
instructions = [(int(parts[1]), int(parts[3]), int(parts[5])) for instruction in instructions for parts in [instruction.split(' ')]]

for instruction in instructions:
    stacks_dict = make_a_move(stacks_dict,instruction)
top_crates=''
for pile in stacks_dict:
    top_crates += stacks_dict[pile].pop()
print(top_crates)
