from collections import Counter

def remove_duplicates(numbers: list[int]) -> list[int]:
    c = Counter(numbers)
    result = []
    for i in range(len(numbers)):
        n = numbers[i]
        if c[n] <= 1:
            result.append(n)
    return result