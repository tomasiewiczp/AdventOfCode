# task url: https://adventofcode.com/2023/day/1
import re

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return read_hook.readlines()

input_values = read_input_file("input.txt")
values = [int(digits[0][0] + digits[-1][-1]) for line in input_values if (digits := re.findall(r'[0-9]+', line))]

print(sum(values))
