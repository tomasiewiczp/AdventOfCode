# task url: https://adventofcode.com/2024/day/2
import numpy as np

def is_safe(report):
    differences = np.diff(report)
    return all(1 <= diff <= 3 for diff in differences) or all(-3 <= diff <= -1 for diff in differences)

with open('input.txt', 'r') as file:
    reports = [tuple(map(int, line.strip().split())) for line in file]
    
print(sum(is_safe(report) for report in reports))