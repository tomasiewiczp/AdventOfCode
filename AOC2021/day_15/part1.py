# task url: https://adventofcode.com/2021/day/15
import heapq

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return [[int(val) for val in line.strip()] for line in   read_hook.readlines()]


board = read_input_file('input.txt')
rows, cols = len(board), len(board[0])

#costs board - lowest found cost of achiving this field
costs = [[float('inf')] * cols for _ in range(rows)]
costs[0][0] = 0
moves_stack = [(0, (0,0))]

while moves_stack:
    curr_cost, (x, y) = heapq.heappop(moves_stack)
    if (x, y) == (rows-1, cols-1):
        print(curr_cost)
        break
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            new_cost = curr_cost + board[nx][ny]
            if new_cost < costs[nx][ny]:
                costs[nx][ny] = new_cost
                heapq.heappush(moves_stack, (new_cost, (nx, ny)))