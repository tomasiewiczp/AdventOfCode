# task url: https://adventofcode.com/2022/day/4
import re

def read_input_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

total_sum = 0
for pairs in read_input_file('input.txt'):
    boundaries = [int(num) for num in re.split('-|,', pairs)]
    if (boundaries[0] >= boundaries[2] and boundaries[1] <= boundaries[3]) or (boundaries[0] <= boundaries[2] and boundaries[1] >= boundaries[3]):
        total_sum += 1

print(total_sum)