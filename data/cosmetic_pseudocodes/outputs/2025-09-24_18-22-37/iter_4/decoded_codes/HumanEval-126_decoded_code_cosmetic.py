from typing import List


def is_sorted(list_of_numbers: List[int]) -> bool:
    frequency_map: dict[int, int] = {}
    idx: int = 0
    while idx < len(list_of_numbers):
        element = list_of_numbers[idx]
        frequency_map[element] = frequency_map.get(element, 0) + 1
        idx += 1

    key_list: List[int] = list_of_numbers
    duplicate_found: bool = False
    k: int = 0
    while k < len(key_list) and not duplicate_found:
        if frequency_map[key_list[k]] > 2:
            duplicate_found = True
        k += 1

    if duplicate_found:
        return False

    index: int = 1
    sorted_order: bool = True
    while index < len(list_of_numbers) and sorted_order:
        if list_of_numbers[index - 1] > list_of_numbers[index]:
            sorted_order = False
        index += 1

    if sorted_order:
        return True
    else:
        return False