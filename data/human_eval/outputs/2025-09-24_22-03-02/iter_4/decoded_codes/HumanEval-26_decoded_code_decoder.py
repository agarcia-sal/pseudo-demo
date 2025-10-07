from typing import List
import collections

def remove_duplicates(numbers: List[int]) -> List[int]:
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]