from collections import Counter

def remove_duplicates(numbers):
    count = Counter(numbers)
    return [number for number in numbers if count[number] <= 1]