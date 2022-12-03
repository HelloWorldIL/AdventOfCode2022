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

def get_top_foods(elves, count=1):
    sums = []
    for foods in elves:
        sums.append(sum(foods))
    return sorted(sums, reverse=True)[:count]

foods = get_elfs_food()
top_food_sums = get_top_foods(foods, 3)
print(sum(top_food_sums))
