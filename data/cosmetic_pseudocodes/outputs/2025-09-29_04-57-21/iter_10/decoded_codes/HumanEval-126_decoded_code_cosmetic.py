from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    frequency_map: dict[int, int] = {}
    for element in list_of_numbers:
        frequency_map[element] = frequency_map.get(element, 0) + 1

    for element in list_of_numbers:
        if frequency_map[element] > 2:
            return False

    for pos in range(1, len(list_of_numbers)):
        if list_of_numbers[pos - 1] > list_of_numbers[pos]:
            return False

    return True