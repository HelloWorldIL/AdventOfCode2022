ROCK = 1
PAPER = 2
SCISSORS = 3

BEAT_MAP = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK
}

ENCRYPTION_MAP = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS,

    'X': ROCK,
    'Y': PAPER,
    'Z': SCISSORS
}

def get_encrypted_guide(path='input.txt'):
    with open(path, 'r') as fd:
        rounds = []
        for line in fd:
            if line == '\n' or line == '': break
            rounds.append(line.rstrip().split(' '))
        return rounds

def _decrypt_guide_row(encrypted_row):
    opponent = ENCRYPTION_MAP[encrypted_row[0]]
    own = ENCRYPTION_MAP[encrypted_row[1]]

    return (opponent, own)

def decrypt_guide(encrypted_guide):
    guide = []
    for row in encrypted_guide:
        guide.append(_decrypt_guide_row(row))
    return guide

def get_round_result(opponent, own):
    if BEAT_MAP[opponent] == own: # win
        return 6
    if BEAT_MAP[own] == opponent: # lose
        return 0
    return 3 # draw

def calculate_round_points(opponent, own):
    result = get_round_result(opponent, own)
    return own + result

def calculate_total_points(guide):
    total = 0
    for round in guide:
        total += calculate_round_points(*round)
    return total

encrypted_guide = get_encrypted_guide()
guide = decrypt_guide(encrypted_guide)
print(calculate_total_points(guide))
