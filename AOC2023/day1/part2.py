# task url: https://adventofcode.com/2023/day/1
import regex # using regex instead of re to cover overlapping cases, as some number words might overlap (e.g., 'oneight' contains both 'one' and 'eight')

# Dictionary mapping words to numbers from 0 to 9
word_to_number = {
    "one"   : "1",
    "two"   : "2",
    "three" : "3",
    "four"  : "4",
    "five"  : "5",
    "six"   : "6",
    "seven" : "7",
    "eight" : "8",
    "nine"  : "9"
}

def read_input_file(file_path):
    with open(file_path) as read_hook:
        return read_hook.readlines()

def convert_str_to_num(value, first = True):
    if value in word_to_number:
        return word_to_number[value]
    elif first:
        return value[0]
    return value[-1]

words_pattern = "|".join(word_to_number.keys())
regex_pattern = rf'{words_pattern}|\d+'
numbers= []
for line in read_input_file("input.txt"):
    potential_values = regex.findall(regex_pattern, line, overlapped=True)
    numbers.append(int(convert_str_to_num(potential_values[0])+ convert_str_to_num(potential_values[-1], False)))
print(sum(numbers))
