import os
PATH=os.getcwd()+'/day_8/input.txt'

def load_input(path):
    with open(path,'r') as file:
        return file.readlines()

class Node:
    def __init__(self, input_info):
        self.node_name = input_info.split(' = ')[0]
        self.pairs = input_info.split(' = ')[1][1:-1].split(', ')

    def __getitem__(self, site):
        if site == 'L':
            return self.pairs[0]
        elif site == 'R':
            return self.pairs[1]

class Map:
    def __init__(self,nodes):
        self.map={}
        for node in nodes:
            self.map[node.node_name]=node

    def __getitem__(self,name):
        return self.map[name]

input = load_input(PATH)
instructions = input[0].strip()
print(instructions)
map=Map([Node(num.strip()) for num in input[2:]])
count=0
node=map['AAA']
cont=True
while cont:
    for instruction in instructions:
        next_node=node[instruction]
        count+=1
        if next_node=='ZZZ':
            cont=False
            break
        node=map[next_node]
print(count)