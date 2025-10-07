from typing import Iterable, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: Iterable[T]) -> T:
    iterator = iter(list_of_elements)
    maximum_element = next(iterator)  # Raises StopIteration if empty
    for element in iterator:
        if element > maximum_element:
            maximum_element = element
    return maximum_element