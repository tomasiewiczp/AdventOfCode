# task url: https://adventofcode.com/2024/day/1
from collections import Counter

with open('input.txt', 'r') as file:
    lists = [tuple(map(int, line.strip().split())) for line in file]
    left = [line[0] for line in lists]
    right = Counter([line[1] for line in lists])
    similarity_score = sum([num*right[num] for num in left])
    print(similarity_score)