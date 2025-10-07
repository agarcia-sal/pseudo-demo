from typing import List, TypeVar

T = TypeVar('T')

def monotonic(l: List[T]) -> bool:
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    else:
        return False