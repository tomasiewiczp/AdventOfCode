import json

# Load input file
with open('input.txt') as f:
    inputs = [json.loads(line) for line in f]

# Add value after explode to left branch
def add_leftmost(number, value):
    if isinstance(number, int):
        return number + value
    left, right = number
    return [add_leftmost(left, value), right]

# Add value after explode to right branch
def add_rightmost(number, value):
    if isinstance(number, int):
        return number + value
    left, right = number
    return [left, add_rightmost(right, value)]

# Funkcja explode - immutable styl
def explode(number, depth=0):
    if isinstance(number, int):
        return False, number, None, None

    left, right = number

    if depth == 4:
        # explodes here
        return True, 0, left, right

    #left side explosion check
    exploded, new_left, lcarry, rcarry = explode(left, depth+1)
    if exploded:
        if rcarry is not None:
            right = add_leftmost(right, rcarry) #add right value to the right 
        return True, [new_left, right], lcarry, None

    #right side explosion check
    exploded, new_right, lcarry, rcarry = explode(right, depth+1)
    if exploded:
        if lcarry is not None:
            left = add_rightmost(left, lcarry)
        return True, [left, new_right], None, rcarry

    return False, [left, right], None, None

def split(number):
    if isinstance(number, int):
        if number >= 10:
            return True, [number // 2, (number + 1) // 2]
        else:
            return False, number
    left, right = number
    changed, new_left = split(left)
    if changed:
        return True, [new_left, right]
    changed, new_right = split(right)
    if changed:
        return True, [left, new_right]
    return False, [left, right]

def reduce(number):
    while True:
        changed, number, _, _ = explode(number)
        if changed:
            continue
        changed, number = split(number)
        if changed:
            continue
        break
    return number

def snailfish_add(left, right):
    return reduce([left, right])

def magnitude(number):
    if isinstance(number, int):
        return number
    left, right = number
    return 3 * magnitude(left) + 2 * magnitude(right)


from copy import deepcopy
from itertools import permutations

combinations = [list(comb) for comb in permutations(inputs, 2)]
max_magnitude = 0
for combination in combinations:
    left,right = deepcopy(combination)
    max_magnitude = max(max_magnitude, magnitude(snailfish_add(left,right)))
print(max_magnitude)