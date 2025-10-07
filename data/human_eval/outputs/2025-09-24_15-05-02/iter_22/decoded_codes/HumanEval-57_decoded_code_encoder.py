from typing import List, TypeVar

T = TypeVar('T')

def monotonic(list_of_values: List[T]) -> bool:
    if list_of_values == sorted(list_of_values) or list_of_values == sorted(list_of_values, reverse=True):
        return True
    return False