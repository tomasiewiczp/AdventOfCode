import os
PATH=os.getcwd()+'/day_7/input.txt'
CARDS=('2','3','4','5','6','7','8','9','T','J','Q','K','A')

def load_input(path):
    with open(path,'r') as file:
        return file.readlines()

class Hand:
    def __init__(self,input):
        self.cards=input[0]
        self.score=int(input[1])
        self.strenght=self.__find_strenght__()
    
    def __find_strenght__(self):
        # strenght for higher cards=0, for pair =1, for 2 pairs =2, for 3=3, for full 3,5 for 4=4 for 5 =5
        cards=self.cards
        amounts=[]
        for card in cards:
            amounts.append(cards.count(card))
            cards=cards.replace(card,'')
        if max(amounts)>3:
            return max(amounts)
        elif max(amounts)==3:
            if 2 in amounts:
                return 3.5
            return 3
        elif max(amounts)==2:
            if amounts.count(2)>1:
                return 2
            return 1
        return 0
            
    def __gt__(self,other_hand):
        if self.strenght!=other_hand.strenght:
            return self.strenght>other_hand.strenght
        else:
            for num,card in enumerate(self.cards):
                if card!=other_hand.cards[num]:
                    return CARDS.index(card)>CARDS.index(other_hand.cards[num])
  
input = [i.strip().split() for i in load_input(PATH)]
hands=[]
for hand in input:
    hands.append(Hand(hand))
hands.sort()
result=0
for num,hand in enumerate(hands):
    result+=(num+1)*hand.score
print(result)