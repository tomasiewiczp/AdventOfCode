# task url: https://adventofcode.com/2022/day/6

def read_input_file(file_path):
    with open(file_path, "r") as file:
        return file.readline()

signal = read_input_file("input.txt")
for number in range(3,len(signal)):
    if len(set(signal[number-4:number]))==4:
        print(number)
        break