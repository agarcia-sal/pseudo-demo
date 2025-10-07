from typing import List, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: List[T]) -> T:
    idx: int = 0
    length: int = len(list_of_elements)
    max_value: T = list_of_elements[0]
    while idx < length:
        current_item: T = list_of_elements[idx]
        if current_item > max_value:
            max_value = current_item
        idx += 1
    return max_value