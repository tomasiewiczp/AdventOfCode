import re

class CodeProcessor:
    def __init__(self, path):
        self.path = path
        self.data = self.load_input()
        self.line_len = len(self.data[0])
        self.sum = 0

    def load_input(self):
        with open(self.path, 'r') as file:
            return file.readlines()

    def process_code(self):
        prev_numbers = []
        this_line_numbers = [(match.span()[0] - 1, match.span()[1]) for match in re.finditer(r"\d+", self.data[0])]

        prev_values = []
        this_values = [match.group() for match in re.finditer(r"\d+", self.data[0])]
        for i in range(len(self.data)):
            next_numbers = [(match.span()[0] - 1, match.span()[1]) for match in re.finditer(r"\d+", self.data[i + 1 if i != self.line_len - 2 else i])]
            next_values = [match.group() for match in re.finditer(r"\d+", self.data[i + 1 if i != self.line_len - 2 else i])]
            numbers_positions = prev_numbers + this_line_numbers + next_numbers
            numbers = prev_values + this_values + next_values
            asterisks = [match.start() for match in re.finditer(r"\*", self.data[i])]

            if asterisks != ([], 0):
                for ast in asterisks:
                    counter = 0
                    enums = []
                    for count, numbers_pos in enumerate(numbers_positions):
                        if ast >= numbers_pos[0] and ast <= numbers_pos[1]:
                            counter += 1
                            enums.append(int(numbers[count]))
                    if counter == 2:
                        self.sum += (enums[0] * enums[1])

            prev_numbers = this_line_numbers
            this_line_numbers = next_numbers
            prev_values = this_values
            this_values = next_values
        print(self.sum)

code_processor = CodeProcessor('day_3/input2.txt')
code_processor.process_code()