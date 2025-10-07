from typing import List, TypeVar

T = TypeVar('T')

def maximum(x1: List[T], y2: int) -> List[T]:
    if y2 == 0:
        return []
    x1_sorted = sorted(x1)
    return x1_sorted[-y2:]