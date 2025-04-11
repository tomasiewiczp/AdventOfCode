# task url: https://adventofcode.com/2021/day/1

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return [int(line) for line in read_hook.readlines()]

depths = read_input_file("input.txt")
depth_diff = (depths[i+3] - depths[i] for i in range(0, len(depths)-3))
# I used the fact that 2 out of three values in the comparing windows are the same - no sum needed
print(sum(1 for diff in depth_diff if diff > 0))