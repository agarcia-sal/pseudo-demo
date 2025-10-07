from typing import TypeVar, Sequence

T = TypeVar('T')

def max_element(list_of_elements: Sequence[T]) -> T:
    strongest_candidate = list_of_elements[0]
    for index in range(1, len(list_of_elements)):
        current_value = list_of_elements[index]
        if not (current_value <= strongest_candidate):
            strongest_candidate = current_value
    return strongest_candidate