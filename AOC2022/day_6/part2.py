# task url: https://adventofcode.com/2022/day/6

def read_input_file(file_path):
    with open(file_path, "r") as file:
        return file.readline()

signal = read_input_file("input.txt")
for number in range(13,len(signal)):
    if len(set(signal[number-14:number]))==14:
        print(number)
        break