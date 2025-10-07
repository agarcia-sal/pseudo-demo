from typing import List, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: List[T]) -> T:
    if not list_of_elements:
        raise ValueError("max_element() arg is an empty list")
    peak_value: T = list_of_elements[0]
    idx: int = 0
    while idx < len(list_of_elements):
        current_item: T = list_of_elements[idx]
        if current_item > peak_value:
            peak_value = current_item
        idx += 1
    return peak_value