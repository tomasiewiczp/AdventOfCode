import re
PATH='day_3/input2.txt'

def load_input(path):
    with open(path,'r') as file:
        return file.readlines()
    
data=load_input(PATH)
line_len=len(data[0])
sum=0

prev_simbols=[match.span()[0] for match in re.finditer(r"[^\d.\n]", data[0])]
this__line_simbols=[match.span()[0] for match in re.finditer(r"[^\d.\n]", data[1])]

for i in range(len(data)):
    next_simbols=[match.span()[0] for match in re.finditer(r"[^\d.\n]", data[i + 1 if i != line_len-2 else i])]
    positions=set(prev_simbols+this__line_simbols+next_simbols)
    numbers_pos=[match.span() for match in re.finditer(r"\d+", data[i])]
    numbers=[match.group() for match in re.finditer(r"\d+", data[i])]
    for i in range(len(numbers_pos)):
        if any([x in positions for x in range(numbers_pos[i][0]-1, numbers_pos[i][1]+1)]):
            sum+=int(numbers[i])
    prev_simbols=this__line_simbols
    this__line_simbols=next_simbols
print(sum)