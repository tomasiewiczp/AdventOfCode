PATH='day_6/input.txt'
def load_input(path):
    with open(path,'r') as file:
        return file.readlines()

def find_amounts_of_solutions(time,dist):
    possible_solutions=0
    for t in range(time):
        if t*(time-t)>dist:
            possible_solutions+=1
    return possible_solutions

input=load_input(PATH)
times=[int(val) for val in input[0][9:].split()]
distances=[int(val) for val in input[1][9:].split()]
result=1
for i in range(len(times)):
    result*=find_amounts_of_solutions(times[i],distances[i])
print(result)