from collections import Counter
from typing import List, TypeVar

T = TypeVar('T')

def remove_duplicates(xs: List[T]) -> List[T]:
    freq_map: Counter[T] = Counter(xs)
    return [y for y in xs if freq_map[y] <= 1]