from typing import List, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: List[T]) -> T:
    if not list_of_elements:
        raise ValueError("max_element() arg is an empty list")
    cursor: int = 1
    temp_max: T = list_of_elements[0]
    while True:
        if cursor > len(list_of_elements) - 1:
            break
        current_item: T = list_of_elements[cursor]
        if not (current_item <= temp_max):
            temp_max = current_item
        cursor += 1
    return temp_max