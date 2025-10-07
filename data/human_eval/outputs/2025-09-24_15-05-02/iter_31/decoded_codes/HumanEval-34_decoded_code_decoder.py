from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(list_of_elements: Iterable[T]) -> List[T]:
    return sorted(set(list_of_elements))