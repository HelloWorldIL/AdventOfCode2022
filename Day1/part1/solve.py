def get_elf_food(fd):
    foods = []
    while True:
        line = fd.readline()
        if line == '\n' or line == '': break
        foods.append(int(line))
    return foods

def get_elfs_food(path='input.txt'):
    """Reads from file and returns a list of of lists where each list is all the food items of an elf.

    Yields:
        list[list[int]]: List of elf's food itmes (also a list)
    """
    with open(path, 'r') as fd:
        while True:
            foods = get_elf_food(fd)
            if foods == []: break
            yield foods

def get_highest_food(elves):
    highest = 0
    for foods in elves:
        _sum = sum(foods)
        if _sum > highest:
            highest = _sum
    return highest

foods = get_elfs_food()
print(get_highest_food(foods))
