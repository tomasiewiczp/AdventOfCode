# task url: https://adventofcode.com/2022/day/3

def read_input_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

total_sum = 0

for line in read_input_file('input.txt'):
    stripped_line = line.strip()
    half = len(stripped_line) // 2
    first_comparement = set(stripped_line[:half])
    second_comparement = set(stripped_line[half:])
    common_char = next(iter(first_comparement & second_comparement))
    total_sum += ord(common_char) - (96 if common_char.islower() else 38)

print(total_sum)