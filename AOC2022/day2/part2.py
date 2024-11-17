# task url: https://adventofcode.com/2022/day/1

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return read_hook.readlines()

points_rules = {
    'X':{'score': 0, 'A': 3, 'B': 1, 'C': 2},
    'Y':{'score': 3, 'A': 1, 'B': 2, 'C': 3},
    'Z':{'score': 6, 'A': 2, 'B': 3, 'C': 1}
}
total_score = sum(
            points_rules[mine]['score'] + points_rules[mine][opponent]
            for opponent, mine in (game.split() for game in read_input_file("input.txt"))
        )
print(total_score)