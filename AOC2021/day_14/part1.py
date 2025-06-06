# task url: https://adventofcode.com/2021/day/14
import re
from collections import Counter

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        template = read_hook.readline()
        instructions = [(a, b)  for line in read_hook.readlines()  if line[0].isalpha() for a,b in [line.strip().split('->')]]
        inst={}
        for a,b in instructions:
            inst[a.strip()]=b.strip()
    return template.strip(), inst

def add_letters(instructions, template):
    i=0
    while i < len(template) - 1:
        if template[i:i+2] in instructions:
            template = template[:i+1] + instructions[template[i:i+2]] + template[i+1:]
            i+=1
        i+=1
    return template

template, instructions  = read_input_file('input.txt')
for i in range(10):
    template = add_letters(instructions, template)
cntr = Counter(template)
print(cntr.most_common()[0][1]- cntr.most_common()[-1][1])