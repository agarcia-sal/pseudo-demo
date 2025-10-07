from typing import List
import collections

def remove_duplicates(numbers: List[int]) -> List[int]:
    c = collections.Counter(numbers)
    result: List[int] = []
    i = 0
    while i < len(numbers):
        n = numbers[i]
        if c[n] <= 1:
            result.append(n)
        i += 1
    return result