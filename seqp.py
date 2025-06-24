def can_generate_sequence():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    T = int(data[0])
    index = 1

    results = []

    for _ in range(T):
        N, K = map(int, data[index].split())
        index += 1
        sequence = list(map(int, data[index].split()))
        index += 1

        segments = 1
        for i in range(1, N):
            if sequence[i] != sequence[i - 1]:
                segments += 1


        if segments <= K:
            results.append("YES")
        else:
            results.append("NO")

    for result in results:
        print(result)


if __name__ == "__main__":
    can_generate_sequence()
