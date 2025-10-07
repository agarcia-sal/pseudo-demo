from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    temp_map: dict[int, int] = {}
    for element in list_of_numbers:
        temp_map[element] = temp_map.get(element, 0) + 1

    for count in temp_map.values():
        if count > 2:
            return False

    for idx in range(1, len(list_of_numbers)):
        if list_of_numbers[idx - 1] > list_of_numbers[idx]:
            return False

    return True