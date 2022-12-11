from collections import deque

def get_preamble_index(buff, preamble_size=4):
    window = deque([], maxlen=preamble_size)

    for i, _chr in enumerate(buff):
        if len(set(window)) == preamble_size:
            return i
        window.append(_chr)

with open('input.txt', 'r') as fd:
    buff = fd.read()

print(get_preamble_index(buff, 14))
