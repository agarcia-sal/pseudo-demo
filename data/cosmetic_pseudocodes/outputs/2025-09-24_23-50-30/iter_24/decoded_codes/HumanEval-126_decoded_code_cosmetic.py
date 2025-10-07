from typing import Sequence


def is_sorted(array_of_values: Sequence[int]) -> bool:
    mapping_tracker: dict[int, int] = {}
    for elem in array_of_values:
        mapping_tracker[elem] = mapping_tracker.get(elem, 0) + 1
    for elem_check in array_of_values:
        if mapping_tracker[elem_check] > 2:
            return False
    ptr: int = 1
    while ptr < len(array_of_values):
        if array_of_values[ptr - 1] > array_of_values[ptr]:
            return False
        ptr += 1
    return True