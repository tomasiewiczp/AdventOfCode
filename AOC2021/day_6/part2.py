# task url: https://adventofcode.com/2021/day/5
from collections import Counter, defaultdict

BOARD_SIZE = 1000
def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return [int(val) for val in read_hook.readlines()[0].split(',')]

star_fish_age = defaultdict(int,(Counter(read_input_file('input.txt'))))
for iter in range(80):
    newborn = star_fish_age[0]
    for key in range(1,9):
       star_fish_age[key-1] = star_fish_age[key]
    star_fish_age[6]+=newborn
    star_fish_age[8]=newborn
print(sum(star_fish_age.values()))