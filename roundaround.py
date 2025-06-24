import sys

def custom_round(number, ndigits):
    factor = 10 ** ndigits
    return (number + factor // 2) // factor * factor

def chain_round(number, b):
    for i in range(1, b + 1):
        number = custom_round(number, i)
    return number

def powered(number):
    power = 0
    while number >= 10:
        number //= 10
        power += 1
    return power

def main():
    input = sys.stdin.read().splitlines()
    T = int(input[0])
    results = []

    for i in range(1, T + 1):
        N = int(input[i])
        power = powered(N)
        amount = 0
        for j in range(2, N + 1):
            direct_round = custom_round(j, power)
            chain_rounded = chain_round(j, power)
            if direct_round != chain_rounded:
                amount += 1
        results.append(amount)

    for result in results:
        print(result)


main()
