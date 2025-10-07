from typing import List


def is_sorted(numbers_array: List[int]) -> bool:
    frequency_map: dict[int, int] = {elem: 0 for elem in numbers_array}

    idx: int = 0
    while idx < len(numbers_array):
        current_val: int = numbers_array[idx]
        frequency_map[current_val] += 1
        idx += 1

    violation_found: bool = False
    position: int = 0

    while position < len(numbers_array):
        candidate: int = numbers_array[position]
        freq_val: int = frequency_map[candidate]
        if freq_val > 2:
            violation_found = True
            break
        position += 1

    if violation_found:
        return False

    if len(numbers_array) <= 1:
        return True

    is_ordered: bool = True
    point: int = 1
    while point < len(numbers_array):
        previous_val: int = numbers_array[point - 1]
        current_val: int = numbers_array[point]
        if previous_val > current_val:
            is_ordered = False
            break
        point += 1

    return is_ordered