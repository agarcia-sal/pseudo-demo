from typing import List, TypeVar

T = TypeVar('T')

def max_element(lst: List[T]) -> T:
    if not lst:
        raise ValueError("max_element() arg is an empty list")
    maximum: T = lst[0]
    for element in lst:
        if element > maximum:
            maximum = element
    return maximum