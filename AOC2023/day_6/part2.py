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
time=int(''.join([val for val in input[0][9:].split()]))
distance=int(''.join([val for val in input[1][9:].split()]))
result=find_amounts_of_solutions(time,distance)
print(result)