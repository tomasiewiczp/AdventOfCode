# task url: https://adventofcode.com/2021/day/3
import pandas as pd

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return [[int(char) for char in line.strip()] for line in read_hook.readlines()]

def find_rating(rating_df, if_ox):
    for i in range(rating_df.shape[1]):
        if if_ox:
            bit_value = (rating_df.sum() >= len(rating_df) / 2).astype(int)[i]
        else:
            bit_value = (rating_df.sum() < len(rating_df) / 2).astype(int)[i]
        rating_df = rating_df[rating_df[i] == bit_value]
        if rating_df.shape[0]==1:
            return int(r''.join(rating_df.iloc[0].astype(str)),2)
            
df = pd.DataFrame(read_input_file('input.txt'))
print(find_rating(df,True)*find_rating(df,False))