from collections import Counter

def filter_unique(numbers):
    freq = Counter(numbers)
    return [n for n in numbers if freq[n] <= 1]