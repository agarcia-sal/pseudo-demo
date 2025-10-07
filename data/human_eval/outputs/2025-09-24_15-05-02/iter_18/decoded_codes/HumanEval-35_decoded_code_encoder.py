from typing import List, TypeVar

T = TypeVar('T')

def max_element(l: List[T]) -> T:
    if not l:
        raise ValueError("max_element() arg is an empty list")
    m: T = l[0]
    for e in l:
        if e > m:
            m = e
    return m