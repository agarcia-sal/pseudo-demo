from typing import List


def is_sorted(list_of_numbers: List[int]) -> bool:
    frequency_map: dict[int, int] = {}
    for current_element in list_of_numbers:
        frequency_map[current_element] = frequency_map.get(current_element, 0) + 1

    if any(count > 2 for count in frequency_map.values()):
        return False

    for i in range(1, len(list_of_numbers)):
        if list_of_numbers[i - 1] > list_of_numbers[i]:
            return False

    return True