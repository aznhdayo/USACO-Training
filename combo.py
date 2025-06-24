"""
ID: azha0561
LANG: PYTHON3
PROG: combo
"""

def generate_valid_settings(n, combo1, combo2):
    def valid_range(value, n):
        valid_positions = []
        for offset in (-2, -1, 0, 1, 2):
            valid_positions.append((value + offset - 1) % n + 1)
        return valid_positions

    valid_settings_list = set()

    for dial1 in valid_range(combo1[0], n):
        for dial2 in valid_range(combo1[1], n):
            for dial3 in valid_range(combo1[2], n):
                valid_settings_list.add((dial1, dial2, dial3))

    for dial1 in valid_range(combo2[0], n):
        for dial2 in valid_range(combo2[1], n):
            for dial3 in valid_range(combo2[2], n):
                valid_settings_list.add((dial1, dial2, dial3))

    return len(valid_settings_list)

with open("combo.in", "r") as fin:
    n = int(fin.readline().strip())

    farmer_combo = list(map(int, fin.readline().strip().replace('_', ' ').split()))
    master_combo = list(map(int, fin.readline().strip().replace('_', ' ').split()))

distinct_settings = generate_valid_settings(n, farmer_combo, master_combo)

with open("combo.out", "w") as fout:
    fout.write(f"{distinct_settings}\n")
