from collections import Counter
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    c = Counter(numbers)
    result = []
    index = 0
    while index < len(numbers):
        n = numbers[index]
        if c[n] <= 1:
            result.append(n)
        index += 1
    return result