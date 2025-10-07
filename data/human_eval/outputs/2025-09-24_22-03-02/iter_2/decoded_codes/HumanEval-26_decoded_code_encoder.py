from collections import Counter

def remove_duplicates(numbers: list[int]) -> list[int]:
    counts = Counter(numbers)
    return [n for n in numbers if counts[n] <= 1]