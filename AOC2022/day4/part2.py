# task url: https://adventofcode.com/2022/day/3
import re

def read_input_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

total_sum = 0
for pairs in read_input_file('input.txt'):
    boundaries = [int(num) for num in re.split('-|,', pairs)]
    start1, end1, start2, end2 = boundaries
    if start1 <= end2 and end1 >= start2:
        total_sum += 1

print(total_sum)