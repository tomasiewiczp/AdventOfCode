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

#use only vertical or horizontal instructions 
df = df[(df['x1'] == df['x2']) | (df['y1'] == df['y2'])]

#put marks on the board
for _, row in df.iterrows():
    x1, y1, x2, y2 = row
    board.loc[min(y1,y2):max(y1,y2), min(x1,x2):max(x1,x2)] += 1
print((board >1).values.sum()) #works because values treats True as 1