from typing import List, TypeVar

T = TypeVar('T')

def unique(list_input: List[T]) -> List[T]:
    return sorted(list(set(list_input)))