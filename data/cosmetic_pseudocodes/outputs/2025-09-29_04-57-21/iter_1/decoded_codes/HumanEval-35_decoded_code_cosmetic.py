from typing import TypeVar, Sequence

T = TypeVar('T')

def max_element(list_of_elements: Sequence[T]) -> T:
    if not list_of_elements:
        raise ValueError("max_element() arg is an empty sequence")
    current_max: T = list_of_elements[0]
    for index in range(1, len(list_of_elements)):
        item = list_of_elements[index]
        if current_max < item:
            current_max = item
    return current_max