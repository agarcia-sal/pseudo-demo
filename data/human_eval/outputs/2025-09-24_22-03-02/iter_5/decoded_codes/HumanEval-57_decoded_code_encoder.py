from typing import List, TypeVar

T = TypeVar('T', bound='Comparable')

def monotonic(l: List[T]) -> bool:
    return l == sorted(l) or l == sorted(l, reverse=True)