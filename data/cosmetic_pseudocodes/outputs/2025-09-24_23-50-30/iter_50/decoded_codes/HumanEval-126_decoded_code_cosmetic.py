from typing import Sequence, TypeVar

T = TypeVar('T')

def is_sorted(sequence: Sequence[T]) -> bool:
    frequency_map: dict[T, int] = {}
    temp_index: int = 0

    while temp_index < len(sequence):
        current_element = sequence[temp_index]
        if current_element not in frequency_map:
            frequency_map[current_element] = 1
        else:
            frequency_map[current_element] += 1
        temp_index += 1

    for element_key in frequency_map.keys():
        if frequency_map[element_key] > 2:
            return False

    validate_index: int = 1
    monotonic_flag: bool = True

    while validate_index < len(sequence) and monotonic_flag:
        if not (sequence[validate_index - 1] <= sequence[validate_index]):
            monotonic_flag = False
        validate_index += 1

    if monotonic_flag:
        return True
    return False