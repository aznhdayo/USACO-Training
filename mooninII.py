import sys

def count_distinct_moos(arr):
    moos = set()
    n = len(arr)

    for i in range(n - 2):
        first = arr[i]
        for j in range(i + 1, n - 1):
            second = arr[j]
            if first != second:
                for k in range(j + 1, n):
                    third = arr[k]
                    if second == third:
                        moos.add((first, second, third))
    return len(moos)


input_data = sys.stdin.read().split()
N = int(input_data[0])
arr = list(map(int, input_data[1:]))
print(count_distinct_moos(arr))

