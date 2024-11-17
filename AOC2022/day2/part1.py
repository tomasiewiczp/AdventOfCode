# task url: https://adventofcode.com/2022/day/1

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return read_hook.readlines()

points_rules = {
    'X':{'score': 1, 'A': 3, 'B': 0, 'C': 6},
    'Y':{'score': 2, 'A': 6, 'B': 3, 'C': 0},
    'Z':{'score': 3, 'A': 0, 'B': 6, 'C': 3}
}
total_score = sum(
            points_rules[mine]['score'] + points_rules[mine][opponent]
            for opponent, mine in (game.split() for game in read_input_file("input.txt"))
        )
print(total_score)