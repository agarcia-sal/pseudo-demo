from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(array_of_values: Sequence[T]) -> T:
    index_tracker: int = 1
    largest_value: T = array_of_values[0]
    while index_tracker < len(array_of_values):
        if array_of_values[index_tracker] > largest_value:
            largest_value = array_of_values[index_tracker]
        # No-op case implicitly handled by doing nothing
        index_tracker += 1
    return largest_value