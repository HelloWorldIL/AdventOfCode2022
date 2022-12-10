def get_assignments(path='input.txt'):
    assignments = []
    with open(path) as fd:
        for line in fd:
            line = line.rstrip()
            pairs = line.split(',')
            assignments.append(tuple(list(map(int, elf.split('-'))) for elf in pairs))

    return assignments

def _get_contained(first_range, second_range):
    """Checks if `second_range` is contained within `first_range`
    a range is an iterable that describes a range of items, examples:
    (1, 5)
    [3, 9]
    (0, 1)
    [-5, 5]

    Args:
        first_range (iterable): The first range
        second_range (_type_): The second range

    Returns:
        bool: True if `second_range` is contained within `first_range`, False otherwise
    """
    if second_range[0] >= first_range[0] and second_range[1] <= first_range[1]:
        return True
    return False

def get_contained(ranges):
    if _get_contained(*ranges):
        return 1
    if _get_contained(*ranges[::-1]):
        return 0

assignments = get_assignments()
count = 0
for assignment in assignments:
    if get_contained(assignment) != None:
        count += 1

print(count)