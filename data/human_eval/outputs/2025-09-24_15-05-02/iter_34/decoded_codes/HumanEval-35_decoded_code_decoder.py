from typing import TypeVar, Sequence

T = TypeVar('T')

def max_element(list_of_elements: Sequence[T]) -> T:
    maximum_element = list_of_elements[0]
    for element in list_of_elements:
        if element > maximum_element:
            maximum_element = element
    return maximum_element