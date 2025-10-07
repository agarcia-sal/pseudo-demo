from typing import List, TypeVar

T = TypeVar('T')

def max_element(list_l: List[T]) -> T:
    m = list_l[0]
    for e in list_l:
        if e > m:
            m = e
    return m