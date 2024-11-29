# task url: https://adventofcode.com/2022/day/9

movements = {
    'R' : (0, 1),
    'L' : (0, -1),
    'U' : (1, 0),
    'D' : (-1, 0)
}

def read_input_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

def find_new_tail_pos(head_pos, tail_pos, movement):
    if abs(head_pos[0]-tail_pos[0]) <= 1 and abs(head_pos[1]-tail_pos[1]) <=1:
        return tail_pos
    return (head_pos[0]- movement[0], head_pos[1]- movement[1])

instructions = [line.split() for line in read_input_file("input.txt")]
positions = [0]
head_pos = tail_pos = [0,0]
for instruction in instructions:
    movement = movements[instruction[0]]
    for move in range(int(instruction[1])):
        head_pos = [ head_pos[0] + movement[0], head_pos[1] + movement[1]]
        tail_pos = find_new_tail_pos(head_pos, tail_pos, movement)
        positions.append(tail_pos[0]*1000+tail_pos[1])

print(len(set(positions)))