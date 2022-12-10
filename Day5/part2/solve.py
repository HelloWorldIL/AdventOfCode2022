from collections import deque

def get_num_of_stacks(fd):
    line = fd.readline()
    line_length = len(line)
    num_of_stacks = (line_length+1)//4
    fd.seek(0)
    return num_of_stacks

def get_expected_end_line(num_of_stacks):
    return ' '.join(map(' {} '.format, list(range(1, num_of_stacks+1))))

def insert_crates(line, arrangement, num_of_stacks):
    for i in range(num_of_stacks):
        crate = line[1+(i*4)]
        if crate != ' ':
            arrangement[i].append(crate)

def get_initial_arrangement(fd):
    num_of_stacks = get_num_of_stacks(fd)
    expected_end_line = get_expected_end_line(num_of_stacks)
    arrangement = [deque() for _ in range(num_of_stacks)]
    for line in fd:
        line = line.rstrip('\n')
        if line == expected_end_line:
            return arrangement
        insert_crates(line, arrangement, num_of_stacks)

def get_moves(fd):
    moves = []
    for line in fd:
        line = line.rstrip('\n')
        moves.append(get_move(line))
    return moves

def _get_command_num(line: str, command: str):
    start = line.find(command)+len(command)+1
    end = line.find(' ', start)
    if end == -1:
        end = None
    return int(line[start:end])

def get_move(line: str):
    _count = _get_command_num(line, 'move')
    _from = _get_command_num(line, 'from')
    _to = _get_command_num(line, 'to')
    return (_count, _from, _to)

def do_move(arrangement, move):
    _count, _from, _to = move
    _from = _from-1
    _to = _to-1
    temp = []
    for _ in range(_count):
        temp.append(arrangement[_from].popleft())
    temp.reverse()
    arrangement[_to].extendleft(temp)

def get_top(arrangement):
    x = ''
    for i in range(len(arrangement)):
        if len(arrangement[i]) == 0:
            x+=' '
        else:
            x += arrangement[i][0]
    return x


path='input.txt'
fd = open(path)
arrangement = get_initial_arrangement(fd)
fd.readline()
moves = get_moves(fd)

for move in moves:
    do_move(arrangement, move)

print(get_top(arrangement))
