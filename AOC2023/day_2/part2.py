# task url: https://adventofcode.com/2023/day/2
import re
from math import prod
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
    
    def return_colour_power(self):
        return prod(self.colours.values())


def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return read_hook.readlines()

input_values = read_input_file("input.txt")

g2 = [Game(line).return_colour_power() for line in input_values]
print(sum(g2))