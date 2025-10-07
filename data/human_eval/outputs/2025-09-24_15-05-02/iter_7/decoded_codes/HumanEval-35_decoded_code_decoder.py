from typing import List, TypeVar

T = TypeVar('T')

def max_element(lst: List[T]) -> T:
    maximum = lst[0]
    for element in lst:
        if element > maximum:
            maximum = element
    return maximum