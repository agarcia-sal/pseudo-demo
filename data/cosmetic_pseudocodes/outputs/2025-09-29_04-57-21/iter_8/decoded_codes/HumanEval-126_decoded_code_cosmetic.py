from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    frequency_map: dict[int, int] = {}
    idx: int = 0
    while idx < len(list_of_numbers):
        elem = list_of_numbers[idx]
        frequency_map[elem] = frequency_map.get(elem, 0) + 1
        idx += 1

    for element in list_of_numbers:
        if frequency_map[element] > 2:
            return False

    position: int = 1
    while position < len(list_of_numbers):
        if not (list_of_numbers[position - 1] <= list_of_numbers[position]):
            return False
        position += 1

    return True