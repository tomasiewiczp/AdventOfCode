# task url: https://adventofcode.com/2021/day/7
import pandas as pd

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return [int(val) for val in read_hook.readlines()[0].split(',')]

crab_postions = pd.DataFrame(read_input_file('input.txt'))
min_fuel_usage = 9e9
for number in range(crab_postions.min().values[0], crab_postions.max().values[0]):
    min_fuel_usage = min(int((crab_postions[0] - number).abs().sum()),min_fuel_usage)
print(min_fuel_usage)