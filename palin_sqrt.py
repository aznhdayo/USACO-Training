"""
ID: azha0561
LANG: PYTHON3
PROG: palsquare
"""
def convert_base(number, base):
    if number == 0:
        return "0"
    digits = []
    while number > 0:
        remainder = number % base
        if remainder >= 10:
            digits.append(chr(ord('A') + remainder - 10))
        else:
            digits.append(str(remainder))
        number //= base
    return ''.join(digits[::-1])

number = 123
base = 16
base_number = convert_base(number, base)
print(f"The number {number} in base {base} is {base_number}")

def is_palindrome(number):
    str_number = str(number)
    return str_number == str_number[::-1]

with open('palsquare.in', 'r') as fin:
    base = int(fin.readline().strip())

nlst = []
for i in range(1, 301):
    square = i ** 2
    base_i = convert_base(i, base)
    base_square = convert_base(square, base)
    if is_palindrome(base_square):
        nlst.append((base_i, base_square))

with open('palsquare.out', 'w') as fout:
    for item in nlst:
        fout.write(f"{item[0]} {item[1]}\n")
