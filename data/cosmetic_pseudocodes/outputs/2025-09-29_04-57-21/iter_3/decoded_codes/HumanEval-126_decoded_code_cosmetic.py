from typing import List


def is_sorted(list_of_numbers: List[int]) -> bool:
    frequency_map: dict[int, int] = {}
    for element in list_of_numbers:
        if element not in frequency_map:
            frequency_map[element] = 0
        frequency_map[element] += 1

    for count in frequency_map.values():
        if count > 2:
            return False

    for i in range(1, len(list_of_numbers)):
        if list_of_numbers[i - 1] > list_of_numbers[i]:
            return False

    return True