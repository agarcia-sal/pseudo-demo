from typing import List
import collections

def remove_duplicates(numbers: List[int]) -> List[int]:
    c = collections.Counter(numbers)
    result = []
    for i in range(len(numbers)):
        n = numbers[i]
        if c[n] <= 1:
            result.append(n)
    return result