# task url: https://adventofcode.com/2021/day/3
import re
import pandas as pd
from itertools import groupby

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return [line.strip() for line in read_hook.readlines()]

def has_bingo(mark_df):
    return (mark_df.all(axis=0).any() or mark_df.all(axis=1).any())

def play_game(instructions, boards):
    for number in instructions:
        for i in range(len(boards)):
            marks[i] = marks[i] | (boards[i] == number)
            if has_bingo(marks[i]):
                board_numeric = boards[i].astype(int)
                unmarked_sum = board_numeric[~marks[i]].sum().sum()
                return int(unmarked_sum*int(number))
            
input = read_input_file('input.txt')
instructions = input[0].split(',')
lines = input[2:]

boards = [
    pd.DataFrame([re.split(r' +', row.strip()) for row in group])
    for is_blank, group in groupby(lines, key=lambda x: x != '')
    if is_blank
]
marks = [pd.DataFrame(False, index=board.index, columns=board.columns) for board in boards]
print(play_game(instructions, boards))

#Example on how does groupby function works:
# lines = [1,2,3,0,1,3,4,5]
# for is_blank, group in groupby(lines, key=lambda x: x>1):
#     print(is_blank)
#     for g in group:
#         print(g)