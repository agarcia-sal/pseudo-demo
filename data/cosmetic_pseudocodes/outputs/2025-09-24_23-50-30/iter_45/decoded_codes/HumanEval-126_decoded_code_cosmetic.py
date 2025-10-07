from typing import List


def is_sorted(list_of_numbers: List[int]) -> bool:
    frequency_map: dict[int, int] = {}
    for element in list_of_numbers:
        frequency_map[element] = frequency_map.get(element, 0) + 1
    for count in frequency_map.values():
        if count > 2:
            return False
    index = 1
    while index < len(list_of_numbers):
        if list_of_numbers[index - 1] > list_of_numbers[index]:
            return False
        index += 1
    return True