from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(list_of_elements: Sequence[T]) -> bool:
    return list_of_elements == sorted(list_of_elements) or list_of_elements == sorted(list_of_elements, reverse=True)