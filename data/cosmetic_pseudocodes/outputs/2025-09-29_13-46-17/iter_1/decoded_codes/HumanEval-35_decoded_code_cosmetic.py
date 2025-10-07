from typing import TypeVar, Sequence

T = TypeVar('T')

def max_element(list_of_elements: Sequence[T]) -> T:
    if not list_of_elements:
        raise ValueError("max_element() arg is an empty sequence")
    maximum_element = list_of_elements[0]
    for element in list_of_elements[1:]:
        if element > maximum_element:
            maximum_element = element
    return maximum_element