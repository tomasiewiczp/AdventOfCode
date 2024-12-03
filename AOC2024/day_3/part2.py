# task url: https://adventofcode.com/2024/day/3
import re
from functools import reduce

def process_element(state, element):
    flag, total = state
    if element.startswith("don't"):
        return False, total
    elif element.startswith("do"):
        return True, total
    elif element.startswith("mul") and state[0]:
        x, y = map(int, re.findall(r"\d+", element))
        return flag, total + (x * y)
    return state

with open('input.txt', 'r') as file:
    line = ''.join(file.readlines())
    
pattern = r"mul\(\s*\d+\s*,\s*\d+\s*\)|do\(\)|don't\(\)"
matches = re.findall(pattern, line)
_, total_sum = reduce(process_element, matches, (True, 0))
print(total_sum)