# task url: https://adventofcode.com/2021/day/7
import pandas as pd

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return [len(signal) for line in read_hook.readlines() for signal in line.split('|')[1].strip().split() ]

signals = pd.DataFrame(read_input_file('input.txt'))
print(sum(signals.isin([2,3,4,7]).values)[0])