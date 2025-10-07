from typing import List, TypeVar

T = TypeVar('T')

def max_element(lst: List[T]) -> T:
    if not lst:
        raise ValueError("max_element() arg is an empty list")
    m = lst[0]
    for e in lst:
        if e > m:
            m = e
    return m