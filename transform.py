"""
ID: azha0561
LANG: PYTHON3
PROG: transform
"""

def rotate_90(matrix):
    N = len(matrix)
    rotated = [['' for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotated[j][N - i - 1] = matrix[i][j]
    return rotated

def reflect(matrix):
    return [row[::-1] for row in matrix]

def is_equal(matrix1, matrix2):
    return matrix1 == matrix2

def determine_transformation(before, after):
    transformations = [
        rotate_90(before),
        rotate_90(rotate_90(before)),
        rotate_90(rotate_90(rotate_90(before))),
        reflect(before),
        rotate_90(reflect(before)),
        rotate_90(rotate_90(reflect(before))),
        rotate_90(rotate_90(rotate_90(reflect(before))))
    ]

    if is_equal(transformations[0], after):
        return 1
    if is_equal(transformations[1], after):
        return 2
    if is_equal(transformations[2], after):
        return 3
    if is_equal(transformations[3], after):
        return 4
    if is_equal(transformations[4], after):
        return 5
    if is_equal(transformations[5], after):
        return 5
    if is_equal(transformations[6], after):
        return
    if is_equal(before, after):
        return 6
    else:
        return 7

def get_pattern(fin, N):
    return [list(fin.readline().strip()) for _ in range(N)]

with open('transform.in', 'r') as fin:
    N = int(fin.readline().strip())
    before = get_pattern(fin, N)
    after = get_pattern(fin, N)

result = determine_transformation(before, after)

with open('transform.out','w') as fout:
	fout.write(f"{result}\n")
