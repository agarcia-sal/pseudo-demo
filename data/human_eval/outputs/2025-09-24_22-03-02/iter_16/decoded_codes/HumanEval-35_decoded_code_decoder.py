from typing import List, TypeVar

T = TypeVar('T')

def max_element(l: List[T]) -> T:
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m