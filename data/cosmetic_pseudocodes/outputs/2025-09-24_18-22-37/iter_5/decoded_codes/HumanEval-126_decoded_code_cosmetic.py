from typing import List, Dict

def is_sorted(list_of_numbers: List[int]) -> bool:
    frequency_map: Dict[int, int] = {num: 0 for num in list_of_numbers}
    idx = 0
    while idx < len(list_of_numbers):
        num = list_of_numbers[idx]
        frequency_map[num] += 1
        idx += 1

    has_excess_duplicates = False
    for key in list_of_numbers:
        if frequency_map[key] > 2:
            has_excess_duplicates = True
            break
    if has_excess_duplicates:
        return False

    position = 1
    sorted_flag = True
    while position < len(list_of_numbers):
        if not (list_of_numbers[position - 1] <= list_of_numbers[position]):
            sorted_flag = False
            break
        position += 1

    return sorted_flag