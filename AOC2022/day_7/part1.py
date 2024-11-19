# task url: https://adventofcode.com/2022/day/7

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
            dir_sizes.append(subdir_size)
    return size

def create_file_system(instructions):
    stack = ["/"]
    file_system = {"/":{}}

    for instruction in instructions[1:]:
        match instruction.split():
            case ["$", "cd", ".."]:
                stack.pop()
            case ["$", "cd", directory] if directory != "..":
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
count_dir_size(file_system['/'])
print(sum([dirs for dirs in dir_sizes if dirs<100000]))