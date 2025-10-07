from typing import List, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: List[T]) -> T:
    if not list_of_elements:
        raise ValueError("max_element() arg is an empty list")
    maximum_element = list_of_elements[0]
    for element in list_of_elements:
        if element > maximum_element:
            maximum_element = element
    return maximum_element