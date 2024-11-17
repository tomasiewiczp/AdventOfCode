# task url: https://adventofcode.com/2023/day/2
import re
from collections import defaultdict

class Game:
    def __init__(self, input_line):
        self.game_number = int(input_line.split()[1][:-1])
        self.rounds_strings = re.findall(r'(\d+)\s+(\w+)', input_line)
        self.colours = defaultdict(int)
        self._fill_colours_dict()

    def _fill_colours_dict(self):
        for number, colour in self.rounds_strings:
            self.colours[colour] = max(self.colours[colour], int(number))
    
    def check_if_valid_game(self, max_settings={"green": 13, "red": 12, "blue": 14}):
        # Using 'any()' to efficiently check if any color value exceeds the maximum setting.
        if any(self.colours[colour] > max_settings[colour] for colour in self.colours):
            return 0
        return self.game_number

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return read_hook.readlines()

input_values = read_input_file("input.txt")

valid_games = filter(lambda game: game != 0, (Game(line).check_if_valid_game() for line in input_values))
print(sum(valid_games))
