from typing import Sequence, TypeVar

T = TypeVar("T", bound="SupportsLessEqual")

class SupportsLessEqual:
    def __le__(self: T, other: T) -> bool:
        ...

def is_sorted(input_array: Sequence[T]) -> bool:
    frequency_map: dict[T, int] = {}
    for index in range(len(input_array)):
        current_element = input_array[index]
        frequency_map[current_element] = frequency_map.get(current_element, 0) + 1

    if any(count > 2 for count in frequency_map.values()):
        return False

    position = 1
    while position < len(input_array):
        if not (input_array[position - 1] <= input_array[position]):
            return False
        position += 1

    return True