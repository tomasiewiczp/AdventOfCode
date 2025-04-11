# task url: https://adventofcode.com/2021/day/2

from collections import defaultdict

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return [(line.split()[0], int(line.split()[1])) for line in read_hook.readlines()]

instructions_summary = defaultdict(int)
for instruction in read_input_file("input.txt"):
    instructions_summary[instruction[0]] += instruction[1]

print(instructions_summary['forward'] * (instructions_summary['down'] - instructions_summary['up']))