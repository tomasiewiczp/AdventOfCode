# task url: https://adventofcode.com/2024/day/5
from collections import defaultdict

def check_update_order(update_order):
    for pos, num in enumerate(update_order):
        if any(int(x) in page_orders[num] for x in update_order[pos:]):
            return False
    return True

def change_order(list_to_reorder):
    for pos,num in enumerate(list_to_reorder):
        last_index = max([i for i, j in enumerate(list_to_reorder[pos:]) if int(j) in  page_orders[num]], default =0)
        if last_index:
            element = list_to_reorder.pop(pos)
            list_to_reorder.insert(last_index+pos,element)

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

order_input = [line.split('|') for line in lines if '|' in line]
updates = [line.split(',') for line in lines if ',' in line]
page_orders = defaultdict(list)
[page_orders[key].append(int(value)) for  value, key in order_input]
wrong_updates = [update for update in updates if not  check_update_order(update)]
for update in wrong_updates:
    while not check_update_order(update):
        change_order(update)
print(sum([int(update[len(update)//2]) for update in wrong_updates]))