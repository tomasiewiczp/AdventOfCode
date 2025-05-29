# task url: https://adventofcode.com/2021/day/13
import re
# from aoc_ocr import convert_6

def read_screen(lines):
    alphabet = {
    " ## #  ##  ######  ##  #": "A",
    "#### #  ######  ###### ": "B",
    " ## #  ##   #   #  # ## ": "C",
    "### #  ##  ##  ##  #### ": "D",
    "#####   ### #   #   ####": "E",
    "#####   ### #   #   #   ": "F",
    " ## #  ##   # ###  # ###": "G",
    "#  ##  ######  ##  ##  #": "H",
    "####  #   #   #   ####  ": "I",
    "  ##   #   #   ##  ##  #": "J",
    "#  ## # ##  # # # # #  #": "K",
    "#   #   #   #   #   ####": "L",
    "#  ###### ## # # # # #  #": "M",
    "#  #### ## # ##  ####  #": "N",
    " ## #  ##  ##  ##  # ## ": "O",
    "### #  ##  #### #   #   ": "P",
    " ## #  ##  ##  ## ## ## ": "Q",
    "### #  ##  #### # # #  #": "R",
    " ### # #    ##    # ### ": "S",
    "#####   #   #   #   #   ": "T",
    "#  ##  ##  ##  ##  # ## ": "U",
    "#  ##  ##  ##  ## #  ## ": "V",
    "#  ##  ##  ## # ## ##  #": "W",
    "#  ## #  #  #  # # #  #": "X",
    "#  ##  ##  #### #   #   ": "Y",
    "####   #  ##  #   #  ####": "Z",
}

    text = ""
    for i in range(0, len(lines[0]), 5):
        block = ''.join(row[i:i+4] for row in lines)
        text += alphabet.get(block, '?')
    return text

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        hashes = [(int(a), int(b))  for line in read_hook.readlines()  if line[0].isdigit() for a,b in [line.strip().split(',')]]
        read_hook.close()
    with open(file_path, "r") as read_hook: 
        instructions = [re.split(r"[ =]",line.strip())[-2:] for line in read_hook.readlines() if line[0].isalpha()]
        return hashes, instructions

def fold(hashes, instruction):
    axis, fold_line = instruction
    moved_points = []
    for x,y in hashes:
        position = int(x) if axis=='x' else int(y)
        new_positions = (2*int(fold_line)-x,y) if axis=='x' else (x,2*int(fold_line)-y)
        if position>int(fold_line):
            moved_points.append(new_positions)
        else:
            moved_points.append((x,y))
    return set(moved_points)


hashes, instructions  = read_input_file('input.txt')
for next_instruction in instructions:
    hashes = fold(hashes, next_instruction)

screen = []
for y in range(max(y for x, y in hashes)+1):
    line = ''
    for x in range(max(x for x, y in hashes)+1):
        if (x,y) in hashes:
            line+='#'
        else:
            line+=' '
    screen.append(line)
print(read_screen(screen))
