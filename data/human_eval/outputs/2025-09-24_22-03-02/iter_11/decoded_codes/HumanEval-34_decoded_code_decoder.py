from typing import List, TypeVar

T = TypeVar('T')

def unique(l: List[T]) -> List[T]:
    return sorted(set(l))