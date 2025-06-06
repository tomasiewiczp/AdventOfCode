# task url: https://adventofcode.com/2021/day/14
import re
from collections import Counter, defaultdict
import copy

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        template = read_hook.readline()
        instructions = [(a, b)  for line in read_hook.readlines()  if line[0].isalpha() for a,b in [line.strip().split('->')]]
        inst={}
        for a,b in instructions:
            inst[a.strip()]= [a[0] + b.strip(),b.strip() + a[1]]
    return template.strip(), inst

def iterate_counters(pairs_counter, instructions):
    new_pairs_counter = defaultdict(int)
    for key in pairs_counter:
        new_pairs_counter[instructions[key][0]]+=pairs_counter[key]
        new_pairs_counter[instructions[key][1]]+=pairs_counter[key]
    return new_pairs_counter

template, instructions  = read_input_file('input.txt')

#start values
pairs_counter = defaultdict(int)
for i in range(len(template)-1):
    pairs_counter[template[i:i+2]]+=1

#iterating
for i in range(40):
    pairs_counter = iterate_counters(pairs_counter, instructions)

#counting numbers
signs_counter = defaultdict(int)
for pair,amount in pairs_counter.items():
    signs_counter[pair[0]]+=amount
    signs_counter[pair[1]]+=amount
print(max(list(signs_counter.values()))//2- min(list(signs_counter.values()))/2) #because the same letter is start and end of pair