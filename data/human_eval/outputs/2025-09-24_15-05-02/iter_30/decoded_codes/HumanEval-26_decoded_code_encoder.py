from collections import Counter
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    c = Counter(numbers)
    return [n for n in numbers if c[n] <= 1]