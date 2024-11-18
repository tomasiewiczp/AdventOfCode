# task url: https://adventofcode.com/2022/day/3

def read_input_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

total_sum = 0
rucksacs = [line.strip() for line in read_input_file('input.txt')]
for line_num in range(2, len(list(rucksacs)), 3):
    line_sets = [set(rucksacs[line_num - i]) for i in range(3)]
    common_char = next(iter(set.intersection(*line_sets)))
    total_sum += ord(common_char) - (96 if common_char.islower() else 38)

print(total_sum)