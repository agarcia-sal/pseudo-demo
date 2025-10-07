from typing import List, Dict


def is_sorted(list_of_numbers: List[int]) -> bool:
    frequency_map: Dict[int, int] = {key: 0 for key in list_of_numbers}
    idx: int = 0
    while idx < len(list_of_numbers):
        current_value = list_of_numbers[idx]
        frequency_map[current_value] += 1
        idx += 1

    has_excess_duplicates: bool = False
    for key in frequency_map:
        if frequency_map[key] > 2:
            has_excess_duplicates = True
            break

    if has_excess_duplicates:
        return False

    ptr: int = 1
    while ptr < len(list_of_numbers):
        if not (list_of_numbers[ptr - 1] <= list_of_numbers[ptr]):
            return False
        ptr += 1

    return True