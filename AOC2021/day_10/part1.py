# task url: https://adventofcode.com/2021/day/10

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return [line.strip() for line in read_hook.readlines()]

def find_corrupted_char(line):
    last_open = []
    for char in line:
        if ord(char) in OPEN:
            last_open.append(ord(char))
        else:
            if ord(char) in (last_open[-1]+1, last_open[-1]+2): #+1 and +2 as I treat these signs as ASCII numbers 
                last_open.pop()
            else:
                return char
    return 0

OPEN = [ord(char) for char in '([{<']
POINTS = {')':3, ']':57, '}':1197, '>':25137}
print(sum([POINTS[find_corrupted_char(line)] for line in read_input_file('input.txt') if find_corrupted_char(line) !=0]))