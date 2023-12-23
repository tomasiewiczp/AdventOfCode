import os
PATH=os.getcwd()+'/day_10/input.txt'
MOVES={
    '|':{'up':(-1,0,'up'), 'down':(1,0,'down')}
    , '-':{'left':(0,-1,'left'), 'right':(0,1,'right')}
    , 'L':{'left':(-1,0,'up'), 'down':((0,1,'right'))}
    , 'J':{'down':(0,-1,'left'), 'right':(-1,0,'up')}
    , '7':{'up':(0,-1,'left'),'right':(1,0,'down')}
    , 'F':{'up':(0,1,'right'),'left':(1,0,'down')}
    }

def load_map(path):
    with open(path,'r') as file:
        input = file.readlines()
        return  [row.strip() for row in input]

class Map:
    def __init__(self, map):
        self.map=map
        self.start_point=self.find_start_pos()
        self.find_first_move()

    def __getitem__(self,position):
        x,y=position
        return self.map[x][y]
    
    def find_start_pos(self):
        for row_number,row in enumerate(self.map):
            if 'S' in row:
                return(row_number,*(i for i, place in enumerate(row) if place == 'S'))

    def find_first_move(self):
        first_moves = {
        (-1, 0): ('up', ['|', '7', 'F']),
        (1, 0): ('down', ['|', 'L', 'J']),
        (0, -1): ('left', ['-', 'L', 'F']), 
        (0, 1): ('right', ['-', '7', 'J'])
        }
        for dx, dy in first_moves:
            if self.map[self.start_point[0] + dx][self.start_point[1] + dy] in first_moves[(dx, dy)][1]:
                self.position = (self.start_point[0] + dx, self.start_point[1] + dy) 
                self.last_move = first_moves[(dx, dy)][0]
                self.steps = 1
                break
  
    def make_move(self):
        next_move=MOVES[self[self.position]][self.last_move]
        self.steps+=1
        self.position=(self.position[0]+next_move[0],self.position[1]+next_move[1])
        self.last_move=next_move[2]
        return self[self.position]!='S'

map=Map(load_map(PATH))
while map.make_move():
    pass
print(map.steps/2)