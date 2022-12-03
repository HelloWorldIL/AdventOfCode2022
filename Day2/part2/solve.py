ROCK = 1
PAPER = 2
SCISSORS = 3

BEAT_MAP = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK
}

ENCRYPTION_OPONENT_MAP = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS,
}

ENCRYPTION_SCORE_MAP = {
    'X': 0, # lose
    'Y': 3, # draw
    'Z': 6 # win
}

def get_encrypted_guide(path='input.txt'):
    with open(path, 'r') as fd:
        rounds = []
        for line in fd:
            if line == '\n' or line == '': break
            rounds.append(line.rstrip().split(' '))
        return rounds

def _decrypt_guide_row(encrypted_row):
    opponent = ENCRYPTION_OPONENT_MAP[encrypted_row[0]]
    score = ENCRYPTION_SCORE_MAP[encrypted_row[1]]

    return (opponent, score)

def decrypt_guide(encrypted_guide):
    guide = []
    for row in encrypted_guide:
        guide.append(_decrypt_guide_row(row))
    return guide

def get_lose_choice(choice):
    """Gets the choice needed to lose
    calculated by removing choices that result in a draw and win:

    `choice = ROCK`

    `{ROCK, PAPER, SCISSORS} - ROCK (draw) - PAPER (win) = SCISSORS (lose)`

    Args:
        choice (int): ROCK, PAPER or SCISSORS
    """
    choices = {ROCK, PAPER, SCISSORS}
    choices = choices - {choice} # draw
    choices = choices - {BEAT_MAP[choice]} # win
    return choices.pop()

def get_choice(opponent, score):
    if score == 0:
        return get_lose_choice(opponent)
    if score == 3:
        return opponent
    if score == 6:
        return BEAT_MAP[opponent]

def calculate_round_points(opponent, score):
    own = get_choice(opponent, score)
    return own + score

def calculate_total_points(guide):
    total = 0
    for round in guide:
        total += calculate_round_points(*round)
    return total

encrypted_guide = get_encrypted_guide()
guide = decrypt_guide(encrypted_guide)
print(calculate_total_points(guide))
