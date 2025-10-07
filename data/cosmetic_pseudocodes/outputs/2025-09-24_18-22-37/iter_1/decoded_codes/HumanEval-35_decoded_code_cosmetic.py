from typing import Iterable, Optional, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: Iterable[T]) -> Optional[T]:
    max_value: Optional[T] = None
    initialized = False
    for element in list_of_elements:
        if not initialized or element > max_value:
            max_value = element
            initialized = True
    return max_value