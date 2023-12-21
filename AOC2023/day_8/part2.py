import os
import math
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
map=Map([Node(num.strip()) for num in input[2:]])
start_nodes=[Node(num.strip()) for num in input[2:] if num[2]=='A']
amounts=[]
for node in start_nodes:
    count=0
    cont=True
    while cont:
        for instruction in instructions:
            next_node=node[instruction]
            count+=1
            if next_node.endswith('Z'):
                cont=False
                amounts.append(count)
                break
            node=map[next_node]
print(math.lcm(*amounts))