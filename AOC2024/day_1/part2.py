# task url: https://adventofcode.com/2024/day/1
from collections import Counter

with open('input.txt', 'r') as file:
    lists = [tuple(map(int, line.strip().split())) for line in file]
    right = Counter(right for _, right in lists)
    similarity_score = sum(left * right[left] for left, _ in lists)
    print(similarity_score)