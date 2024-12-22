# task url: https://adventofcode.com/2024/day/5
from collections import defaultdict

def check_update_order(update_order):
    for pos, num in enumerate(update_order):
        if any(int(x) in page_orders[num] for x in update_order[pos:]):
            return False
    return True

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

order_input = [line.split('|') for line in lines if '|' in line]
updates = [line.split(',') for line in lines if ',' in line]
page_orders = defaultdict(list)
[page_orders[key].append(int(value)) for  value, key in order_input]
print(sum([int(update[len(update)//2]) for update in updates if  check_update_order(update)]))