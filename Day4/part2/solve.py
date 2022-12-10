def get_assignments(path='input.txt'):
    assignments = []
    with open(path) as fd:
        for line in fd:
            line = line.rstrip()
            pairs = line.split(',')
            assignments.append(tuple(list(map(int, elf.split('-'))) for elf in pairs))

    return assignments

def has_overlap(ranges):
    ranges = list(set(range(x[0], x[1]+1)) for x in ranges)
    return len(set.intersection(*ranges)) != 0

assignments = get_assignments()
count = 0
for assignment in assignments:
    if has_overlap(assignment): count += 1

print(count)