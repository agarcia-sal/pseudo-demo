from typing import List
from collections import Counter

def remove_duplicates(numbers: List[int]) -> List[int]:
    c = Counter(numbers)
    result = []
    for n in numbers:
        if c[n] <= 1:
            result.append(n)
    return result