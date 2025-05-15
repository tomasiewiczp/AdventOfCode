# task url: https://adventofcode.com/2021/day/10
from statistics import median

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return [line.strip() for line in read_hook.readlines()]

def find_corrupted_char(line):
    last_open = []
    for char in line:
        if ord(char) in OPEN:
            last_open.append(ord(char))
        else:
            if ord(char) in (last_open[-1]+1, last_open[-1]+2):
                last_open.pop()
            else:
                return 0
    return last_open

def calculate_val(line):
    final_val = 0
    for val in line[::-1]:
        final_val*=5
        final_val+= val
    return final_val

OPEN = [ord(char) for char in '([{<']
POINTS = {40:1, 91:2,123:3, 60:4}
closing_lines_points = [calculate_val([POINTS[value] for value in find_corrupted_char(line)])
                         for line in read_input_file('input.txt') 
                         if find_corrupted_char(line) !=0  ]
print(median(closing_lines_points))