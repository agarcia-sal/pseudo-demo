from collections import Counter

def remove_duplicates(numbers):
    c = Counter(numbers)
    return [n for n in numbers if c[n] <= 1]