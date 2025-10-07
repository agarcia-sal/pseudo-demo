from collections import Counter
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    c = Counter(numbers)
    result = []
    i = 0
    while i < len(numbers):
        n = numbers[i]
        count = c[n]
        if count <= 1:
            result.append(n)
        i += 1
    return result