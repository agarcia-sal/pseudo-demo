from collections import Counter

def remove_duplicates(numbers):
    c = Counter(numbers)
    result = []
    for n in numbers:
        if c[n] <= 1:
            result.append(n)
    return result