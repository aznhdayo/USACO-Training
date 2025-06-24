def count_mismatches(canvas, n):
    mismatches = 0
    for i in range(n // 2):
        for j in range(n // 2):
            cell = canvas[i][j]
            if cell != canvas[i][n - j - 1]:
                mismatches += 1
            if cell != canvas[n - i - 1][j]:
                mismatches += 1
            if cell != canvas[n - i - 1][n - j - 1]:
                mismatches += 1
    return mismatches


def apply_update(canvas, r, c):
    canvas[r][c] = '.' if canvas[r][c] == '#' else '#'


def process_updates(canvas, n, updates):
    results = []
    initial_mismatches = count_mismatches(canvas, n)
    results.append(initial_mismatches)

    for r, c in updates:
        apply_update(canvas, r - 1, c - 1)
        mismatches = count_mismatches(canvas, n)
        results.append(mismatches)

    return results


if __name__ == "__main__":
    import sys

    input = sys.stdin.read
    data = input().strip().split('\n')

    first_line = data[0].split()
    N = int(first_line[0])
    U = int(first_line[1])

    canvas = []
    index = 1
    for i in range(N):
        row = data[index].strip()
        canvas.append([char for char in row])
        index += 1

    updates = []
    for i in range(U):
        r, c = map(int, data[index].strip().split())
        updates.append((r, c))
        index += 1

    results = process_updates(canvas, N, updates)

    for result in results:
        print(result)
