from typing import List, TypeVar

T = TypeVar('T')

def unique(l: List[T]) -> List[T]:
    return sorted(list(set(l)))