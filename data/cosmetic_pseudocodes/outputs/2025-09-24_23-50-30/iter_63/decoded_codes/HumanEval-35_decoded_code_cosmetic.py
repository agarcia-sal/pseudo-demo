from typing import TypeVar, Sequence

T = TypeVar('T')

def max_element(list_of_elements: Sequence[T]) -> T:
    if not list_of_elements:
        raise ValueError("max_element() arg is an empty sequence")
    result: T = list_of_elements[0]
    idx: int = 0
    while idx < len(list_of_elements):
        current = list_of_elements[idx]
        if current > result:
            result = current
        idx += 1
    return result