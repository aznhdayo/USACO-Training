"""
ID: azha0561
LANG: PYTHON3
PROG: dualpal
"""

def to_base(number, base):
    if number == 0:
        return "0"

    digits = []
    while number:
        digits.append(str(number % base))
        number //= base
    return ''.join(reversed(digits))

def is_palindrome(s):
    return s == s[::-1]

with open("dualpal.in", "r") as infile:
    lines = infile.readlines()

output_lines = []

for line in lines:
    num1, num2 = map(int, line.strip().split())
    nums = []
    i = num2 + 1

    while len(nums) < num1:
        count = 0
        for base in range(2, 11):
            if is_palindrome(to_base(i, base)):
                count += 1
            if count >= 2:
                nums.append(i)
                break
        i += 1

    output_lines.extend([str(num) for num in nums])

with open("dualpal.out", "w") as outfile:
    outfile.write("\n".join(output_lines) + "\n")


