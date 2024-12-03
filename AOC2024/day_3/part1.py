# task url: https://adventofcode.com/2024/day/3
import re

with open('input.txt', 'r') as file:
    line = ''.join(file.readlines())
    
pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
matches = re.findall(pattern, line) 
print(sum(int(x)*int(y) for x,y in matches))