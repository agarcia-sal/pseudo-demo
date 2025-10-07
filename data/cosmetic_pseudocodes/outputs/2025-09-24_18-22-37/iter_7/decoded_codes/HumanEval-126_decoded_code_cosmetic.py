from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    frequency_map: dict[int, int] = {}
    for index in range(len(list_of_numbers)):
        current_val = list_of_numbers[index]
        if current_val not in frequency_map:
            frequency_map[current_val] = 0
        frequency_map[current_val] += 1

    violation_found = False
    cursor = 0
    while cursor < len(list_of_numbers):
        check_val = list_of_numbers[cursor]
        if frequency_map[check_val] > 2:
            violation_found = True
            break
        cursor += 1

    if violation_found:
        return False

    idx = 1
    while idx < len(list_of_numbers):
        prev_elem = list_of_numbers[idx - 1]
        curr_elem = list_of_numbers[idx]
        if prev_elem > curr_elem:
            return False
        idx += 1

    return True