from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(array_input: Sequence[T]) -> T:
    if not array_input:
        raise ValueError("max_element() arg is an empty sequence")
    peak_value: T = array_input[0]
    iterator_variable: int = 1
    while iterator_variable < len(array_input):
        current_element: T = array_input[iterator_variable]
        if current_element > peak_value:
            peak_value = current_element
        iterator_variable += 1
    return peak_value