# task url: https://adventofcode.com/2021/day/1

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return [int(line) for line in read_hook.readlines()]

depths = read_input_file("input.txt")
depth_diff = (depths[i] - depths[i-1] for i in range(1, len(depths)))

print(sum(1 for diff in depth_diff if diff > 0))