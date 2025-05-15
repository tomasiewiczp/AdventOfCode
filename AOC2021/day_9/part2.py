# task url: https://adventofcode.com/2021/day/9
import pandas as pd
import math

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return [line.split() for line in read_hook.readlines()]

def check_if_smallest(df,col,row):
    return df[col][row] < min(df[col-1][row], df[col+1][row], df[col][row-1], df[col][row+1])

def check_basin_size(start,df):
    points_to_check = [start]
    basin_points = {start}
    while points_to_check:
        col,row = points_to_check.pop()
        correct_neighbour_points = [point for point in [(col-1,row), (col+1,row), (col,row-1), (col,row+1)] 
            if point[0]*point[1]!=0 
                and point[0]<=sizes[1] 
                and point[0]<=sizes[1] 
                and point[1]<= sizes[0] 
                and df.iloc[ point[1], point[0] ]!=9
                and point not in basin_points]
        basin_points.update(correct_neighbour_points)
        points_to_check.extend(correct_neighbour_points)
    return len(basin_points)

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

#find start points
basin_start_points = [(col,row) for row in range(1,sizes[0]+1) for col in range(1,sizes[1]+1) if check_if_smallest(digits,col,row)]

sizes = sorted([check_basin_size(start, digits) for start in basin_start_points])
print(math.prod(sizes[-3:]))