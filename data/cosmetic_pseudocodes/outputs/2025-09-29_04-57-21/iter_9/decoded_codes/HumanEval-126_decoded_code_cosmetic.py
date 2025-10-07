from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    frequency_map: dict[int, int] = {}
    for element in list_of_numbers:
        frequency_map[element] = frequency_map.get(element, 0) + 1

    if any(count > 2 for count in frequency_map.values()):
        return False

    for idx in range(1, len(list_of_numbers)):
        if list_of_numbers[idx - 1] > list_of_numbers[idx]:
            return False

    return True