from typing import List, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: List[T]) -> T:
    if not list_of_elements:
        raise ValueError("max_element() arg is an empty list")
    p: int = 0
    q: T = list_of_elements[p]
    while p < len(list_of_elements):
        r: T = list_of_elements[p]
        if not (r <= q):
            q = r
        p += 1
    return q