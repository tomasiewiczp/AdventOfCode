# task url: https://adventofcode.com/2022/day/10

def read_input_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

current_value = 1
cycle_values = [0]
instructions = [line.strip().split() for line in read_input_file("input.txt")]
for instruction in instructions:
    if instruction[0]=='noop':
        cycle_values.append(current_value)
    else:
        cycle_values.extend([current_value, current_value])
        current_value += int(instruction[1])
        
print(sum([x*cycle_values[x] for x in range(20,240,40)]))
