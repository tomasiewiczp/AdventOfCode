# task url: https://adventofcode.com/2021/day/5
import pandas as pd
import re
import numpy as np

BOARD_SIZE = 1000
def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return [line.strip() for line in read_hook.readlines()]

#create df with instructions and board
instructions = [re.split(r"->|,",line) for line in read_input_file('input.txt')]
df = pd.DataFrame(instructions, columns = ['x1','y1','x2','y2']).astype(int)
board = pd.DataFrame(np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int))

hor_ver = df[(df['x1'] == df['x2']) | (df['y1'] == df['y2'])]
diagonal = df[~((df['x1'] == df['x2']) | (df['y1'] == df['y2']))]

# put horizontal and vertical marks on the board
for _, row in hor_ver.iterrows():
    x1, y1, x2, y2 = row
    board.loc[min(y1,y2):max(y1,y2), min(x1,x2):max(x1,x2)] += 1

#put diagonal marks on the board
for _, row in diagonal.iterrows():
    x1, y1, x2, y2 = row
    x_sign = (x2-x1) / abs(x2-x1)
    y_sign = (y2-y1) / abs(y2-y1)

    for dif in range(abs(x2-x1)+1):
        board.loc[y1+x_sign*dif, x1+y_sign*dif] += 1
        
print((board >1).values.sum()) #works because values treats True as 1