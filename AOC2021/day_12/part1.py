# task url: https://adventofcode.com/2021/day/12
from collections import defaultdict

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return [line.strip() for line in read_hook.readlines()]

connections = defaultdict(list)
for line in read_input_file('input.txt'):
    a, b = line.split('-')
    connections[a].append(b)
    connections[b].append(a) #connections can work in both ways

paths = [['start']]
finished_paths = []
while paths:
    current_path = paths.pop()
    current_cave = current_path[-1]
    if current_cave == "end":
        finished_paths.append(current_path) #add finished path
        continue
    for move in connections[current_cave]:
        if move.isupper() or move not in current_path:
            paths.append(current_path + [move]) #append all potential next steps 
print(len(finished_paths))