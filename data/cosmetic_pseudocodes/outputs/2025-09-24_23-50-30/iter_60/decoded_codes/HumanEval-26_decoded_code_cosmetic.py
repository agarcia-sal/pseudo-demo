from collections import Counter
from typing import List, Sequence, TypeVar

T = TypeVar('T')

def remove_duplicates(x1: Sequence[T]) -> List[T]:
    x2 = Counter(x1)
    x3: List[T] = []
    x4 = 0
    while x4 < len(x1):
        x5 = x1[x4]
        if x2[x5] <= 1:
            x3.append(x5)
        x4 += 1
    return x3