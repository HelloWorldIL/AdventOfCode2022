def get_backpacks_items(path='input.txt'):
    backpacks = []
    with open(path) as fd:
        for line in fd:
            line = line.rstrip()
            first, second = line[:len(line)//2], line[len(line)//2:]
            backpacks.append((first, second))

    return backpacks

def get_priority(items):
    priorities = []
    for item in items:
        priorities.append(_get_priority(item))
    return priorities

def _get_priority(item: str):
    if not len(item) == 1 or not item.isalpha():
        return
    if item.islower():
        return ord(item)-96
    if item.isupper():
        return ord(item)-38

def get_compartments_duplicates(backpack):
    first, second = set(backpack[0]), set(backpack[1])
    return list(first.intersection(second))


backpacks = get_backpacks_items()
total = 0
for backpack in backpacks:
    duplicates = get_compartments_duplicates(backpack)
    total += sum(get_priority(duplicates))

print(total)
