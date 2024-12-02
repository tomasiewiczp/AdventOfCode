import numpy as np

def is_safe(report):
    differences = np.diff(report)
    return all(1 <= diff <= 3 for diff in differences) or all(-3 <= diff <= -1 for diff in differences)

def is_only_one_wrong(report):
    return any(is_safe(report[:i] + report[i+1:]) for i in range(len(report)))

with open('input.txt', 'r') as file:
    reports = [tuple(map(int, line.strip().split())) for line in file]
    
print(sum(is_safe(report) or is_only_one_wrong(report) for report in reports))