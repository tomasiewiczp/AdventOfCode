# task url: https://adventofcode.com/2024/day/1

with open('input.txt', 'r') as file:
    lists = [list(map(int, line.strip().split())) for line in file]
    l1 = sorted(line[0] for line in lists)
    l2 = sorted(line[1] for line in lists)
    total_distance = sum(abs(l1[i]-l2[i]) for i in range(len(l1)))
    print(total_distance)