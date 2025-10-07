from typing import List


def is_sorted(list_of_numbers: List[int]) -> bool:
    frequency_map: dict[int, int] = {key: 0 for key in list_of_numbers}
    position: int = 0
    while position < len(list_of_numbers):
        current_element = list_of_numbers[position]
        frequency_map[current_element] += 1
        position += 1

    for element in list_of_numbers:
        if frequency_map[element] > 2:
            return False

    idx: int = 1
    while idx < len(list_of_numbers):
        if list_of_numbers[idx - 1] > list_of_numbers[idx]:
            return False
        idx += 1

    return True