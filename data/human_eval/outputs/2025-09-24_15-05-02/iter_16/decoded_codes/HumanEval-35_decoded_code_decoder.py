from typing import List, TypeVar

T = TypeVar('T')

def max_element(lst: List[T]) -> T:
    if not lst:
        raise ValueError("max_element() arg is an empty list")
    max_value: T = lst[0]
    for element in lst:
        if element > max_value:
            max_value = element
    return max_value