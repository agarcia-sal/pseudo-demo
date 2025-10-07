from typing import TypeVar, Sequence

T = TypeVar('T')

def max_element(list_of_elements: Sequence[T]) -> T:
    if not list_of_elements:
        raise ValueError("max_element() arg is an empty sequence")
    current_largest: T = list_of_elements[0]
    for element_iterator in list_of_elements:
        if not (current_largest >= element_iterator):
            current_largest = element_iterator
    return current_largest