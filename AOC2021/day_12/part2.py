from collections import defaultdict

def read_input_file(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]

connections = defaultdict(list)
caves = set()

for line in read_input_file("input.txt"):
    a, b = line.split("-")
    connections[a].append(b)
    connections[b].append(a)
    caves.update([a, b])

small_caves = [c for c in caves if c.islower() and c not in ('start', 'end')]

finished_paths = set()

for double_cave in small_caves:
    paths = [(['start'], False)]  # path + flag if already double used

    while paths:
        current_path, double_used = paths.pop()
        current_cave = current_path[-1]

        if current_cave == 'end':
            finished_paths.add(tuple(current_path))
            continue

        for move in connections[current_cave]:
            if move.isupper() or move not in current_path: #thats where we get with first entrance to double small cave
                paths.append((current_path + [move], double_used))
            elif move == double_cave and not double_used: #thats where we get after the firts entrance
                paths.append((current_path + [move], True))

print(len(finished_paths))