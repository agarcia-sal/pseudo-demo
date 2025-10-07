from typing import List
import collections

def remove_duplicates(numbers: List[int]) -> List[int]:
    c = collections.Counter(numbers)
    result = []
    for n in numbers:
        if c.__getitem__(n) <= 1:
            result.append(n)
    return result