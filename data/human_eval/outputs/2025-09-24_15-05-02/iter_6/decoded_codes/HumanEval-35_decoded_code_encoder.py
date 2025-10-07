from typing import List, TypeVar

T = TypeVar('T')

def max_element(elements: List[T]) -> T:
    maximum = elements[0]
    for element in elements:
        if element > maximum:
            maximum = element
    return maximum