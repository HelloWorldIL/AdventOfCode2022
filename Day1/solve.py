def get_elf_food(fd):
    foods = []
    while True:
        line = fd.readline()
        if line == '\n' or line == '': break
        foods.append(int(line))
    return foods

def get_elf_foods():
    with open('input.txt', 'r') as fd:
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

foods = get_elf_foods()
print(get_highest_food(foods))
