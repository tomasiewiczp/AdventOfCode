PATH='day_4/input2.txt'

class Card:
    def __init__(self,line):
        self.line=line[:-1].split(':')[1].split('|')

    def separate_numbers(self):
        self.winning_numbers={int(num) for num in self.line[0].strip().split()}
        self.got_numbers={int(num) for num in self.line[1].strip().split()}
        return self

    def count_points(self):
        return len(self.winning_numbers.intersection(self.got_numbers))

        
def load_input(path):
    with open(path,'r') as file:
        return file.readlines()
    
data=load_input(PATH)
cards_won=[Card(line).separate_numbers().count_points() for line in data]
final_cards_number=[1]*len(cards_won)
for num,card in enumerate(cards_won):
    for i in range (num+1,num+card+1):
        final_cards_number[i]+=1*final_cards_number[num]
print(sum(final_cards_number))