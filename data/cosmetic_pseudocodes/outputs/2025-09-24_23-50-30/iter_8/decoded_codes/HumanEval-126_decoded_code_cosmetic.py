from typing import Sequence, TypeVar

T = TypeVar('T')

def is_sorted(array_elements: Sequence[T]) -> bool:
    frequency_map: dict[T, int] = {}
    for element in array_elements:
        frequency_map[element] = frequency_map.get(element, 0) + 1
    for key in array_elements:
        if frequency_map[key] > 2:
            return False
    for i in range(1, len(array_elements)):
        if array_elements[i - 1] > array_elements[i]:
            return False
    return True