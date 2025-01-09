# task url: https://adventofcode.com/2024/day/7

def check_possibile_calculations(calculations):
    result, values = calculations
    scores = [values[0]]
    for value in values[1:]:
        scores = [score * value for score in scores] + [score + value for score in scores] + [int(str(score)+str(value)) for score in scores]
    return result in scores

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

results = [int(line.split(':')[0]) for line in lines]
numbers = [[int(num) for num in line.split(':')[1].split()]  for line in lines]
print(sum([pair[0] for pair in zip(results, numbers) if check_possibile_calculations(pair)]))