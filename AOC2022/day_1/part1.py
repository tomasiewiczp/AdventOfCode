# task url: https://adventofcode.com/2022/day/1

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return read_hook.read().strip().split("\n\n")

max_calories =  0
print(read_input_file("input.txt"))
for group in read_input_file("input.txt"):
    current_calories = sum(int(calories) for calories in group.splitlines())
    max_calories = max(max_calories, current_calories)
print(max_calories)