class Player:
    def __init__(self, starting_pos):
        self.current_pos = starting_pos
        self.score = 0
    
    def __check_if_win__(self):
        return self.score>=1000
    
    def make_move(self, dice_number):
        self.current_pos = ((self.current_pos + dice_number - 1) % 10) + 1
        self.score += self.current_pos
        return self.__check_if_win__()
    
class Dice:
    def __init__(self):
        self.roll_number = 0
    
    def roll_dice(self):
        self.roll_number += 1
        return self.roll_number%100


p1 = Player(5)
p2 = Player(9)
dice =  Dice()

while True:
    roll_sum = sum([dice.roll_dice() for _ in range(3)])
    if p1.make_move(roll_sum):
        break
    roll_sum = sum([dice.roll_dice() for _ in range(3)])
    if p2.make_move(roll_sum):
        break

print(min(p1.score, p2.score)*dice.roll_number)