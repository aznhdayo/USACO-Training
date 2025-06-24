"""
ID: azha0561
LANG: PYTHON3
PROG: namenum
"""

import itertools

with open('namenum.in', 'r') as f:
    numbers = f.readline().strip()

thisdict = {
    '2': ['A', 'B', 'C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['J', 'K', 'L'],
    '6': ['M', 'N', 'O'],
    '7': ['P', 'R', 'S'],
    '8': ['T', 'U', 'V'],
    '9': ['W', 'X', 'Y'],
}

with open('dict.txt', 'r') as file:
    valid_names = set(line.strip() for line in file)

number_sequence = numbers

combinations = list(itertools.product(*(thisdict[digit] for digit in number_sequence)))
valid_combinations = []

for combo in combinations:
    name = ''.join(combo)
    if name in valid_names:
        valid_combinations.append(name)

with open('namenum.out', 'w') as f:
    if valid_combinations:
        for name in valid_combinations:
            f.write(f'{name}\n')
    else:
        f.write('NONE\n')
