from typing import List, TypeVar

T = TypeVar('T')

def max_element(list: List[T]) -> T:
    if not list:
        raise ValueError("max_element() arg is an empty list")
    m = list[0]
    for element in list:
        if element > m:
            m = element
    return m