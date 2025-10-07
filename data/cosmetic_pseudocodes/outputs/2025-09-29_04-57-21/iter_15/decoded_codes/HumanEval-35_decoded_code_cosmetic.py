from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: Sequence[T]) -> T:
    if not list_of_elements:
        raise ValueError("max_element() arg is an empty sequence")

    index_counter: int = 0
    largest_value: T = list_of_elements[index_counter]
    while index_counter < len(list_of_elements):
        current_value: T = list_of_elements[index_counter]
        if not (largest_value >= current_value):
            largest_value = current_value
        index_counter += 1
    return largest_value