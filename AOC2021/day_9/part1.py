# task url: https://adventofcode.com/2021/day/9
import pandas as pd

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return [line.split() for line in read_hook.readlines()]

def check_if_smalles(df,col,row):
    return df[col][row] < min(df[col-1][row], df[col+1][row], df[col][row-1], df[col][row+1])

digits = pd.DataFrame([[int(char) for char in row[0]] for row in read_input_file('input.txt')])
sizes = digits.shape
#add rows surrounding table
digits.loc[-1] = digits.loc[0]+1
digits.loc[sizes[0]] = digits.loc[sizes[0]-1]+1
digits = digits.sort_index().reset_index(drop=True) 
#add columns surrounding table
digits.insert(0, -1, digits.iloc[:, 0] + 1) 
digits[digits.shape[1]] = digits.iloc[:, -1] + 1
digits.columns = range(sizes[1]+2)

print(sum([digits[col][row]+1 for row in range(1,sizes[0]+1) for col in range(1,sizes[1]+1) if check_if_smalles(digits,col,row) ]))