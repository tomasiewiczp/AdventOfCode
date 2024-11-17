# task url: https://adventofcode.com/2022/day/1
from heapq import nlargest

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return read_hook.read().strip().split("\n\n")

calories_groups = [sum(int(calories) for calories in group.splitlines()) for group in read_input_file("input.txt")]
print(sum(nlargest(3, calories_groups)))