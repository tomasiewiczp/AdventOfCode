# task url: https://adventofcode.com/2021/day/3
import pandas as pd

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return [[int(char) for char in line.strip()] for line in read_hook.readlines()]

df = pd.DataFrame(read_input_file('input.txt'))
gamma_series = (df.sum() >= len(df) / 2).astype(int)
gamma_bin_number = ''.join(map(str, gamma_series))
print(int(gamma_bin_number, 2)*int(gamma_bin_number.translate(str.maketrans('01', '10')), 2))