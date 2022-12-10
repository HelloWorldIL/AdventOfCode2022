def get_backpacks_items(path='input.txt'):
    backpacks = []
    with open(path) as fd:
        for line in fd:
            line = line.rstrip()
            first, second = line[:len(line)//2], line[len(line)//2:]
            backpacks.append((first, second))

    return backpacks

def _get_priority(item: str):
    if not len(item) == 1 or not item.isalpha():
        return
    if item.islower():
        return ord(item)-96
    if item.isupper():
        return ord(item)-38

def merge_compartments(backpack):
    return backpack[0]+backpack[1]


def find_badge(backpacks, max_group_size=3):
    _backpacks = []
    for backpack in backpacks[:max_group_size]:
        _backpacks.append(set(merge_compartments(backpack)))
    
    # The intersection of all the groups is the badge
    return set.intersection(*_backpacks).pop()

backpacks = get_backpacks_items()
total = 0
for i in range(len(backpacks)//3):
    badge = find_badge(backpacks[i*3:])
    total += _get_priority(badge)
print(total)
