# task url: https://adventofcode.com/2022/day/7
import bisect

def read_input_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

def count_dir_size(file_system):
    size = 0
    for item in file_system.keys():
        if isinstance(file_system[item], int):
            size += file_system[item]
        else:
            subdir_size = count_dir_size(file_system[item])
            size += subdir_size
            bisect.insort(dir_sizes, subdir_size)
    return size


def create_file_system(instructions):
    stack = ["/"]
    file_system = {"/":{}}

    for instruction in instructions[1:]:
        match instruction.split():
            case ["$", "cd", directory]:
                if directory == "..":
                    stack.pop()
                else:
                    stack.append(directory)
            case ["$", "ls"]:
                pass
            case ["dir", directory_name]:
                location = file_system["/"]
                for dir in stack[1:]:
                    location = location[dir]
                location[directory_name] = {}
            case [file_size, file_name]:
                location = file_system["/"]
                for dir in stack[1:]:
                    location = location[dir]
                location[file_name] = int(file_size)
    return file_system

instructions = read_input_file("input.txt")
file_system = create_file_system(instructions)
dir_sizes = []
required_space = count_dir_size(file_system['/']) - 40000000
larger_element = bisect.bisect_right(dir_sizes, required_space)
print(dir_sizes[larger_element])