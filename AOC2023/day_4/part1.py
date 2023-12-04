PATH='day_4/input2.txt'

class Card:
    def __init__(self,line):
        self.line=line[:-1].split(':')[1].split('|')

    def separate_numbers(self):
        self.winning_numbers={int(num) for num in self.line[0].strip().split()}
        self.got_numbers={int(num) for num in self.line[1].strip().split()}

    def count_points(self):
        sum=len(self.winning_numbers.intersection(self.got_numbers))
        return 0 if sum==0 else 1*(2**(sum-1))
        
def load_input(path):
    with open(path,'r') as file:
        return file.readlines()
    
sum=0
data=load_input(PATH)
for line in data:
    l=Card(line)
    l.separate_numbers()
    sum+=l.count_points()
print(sum)