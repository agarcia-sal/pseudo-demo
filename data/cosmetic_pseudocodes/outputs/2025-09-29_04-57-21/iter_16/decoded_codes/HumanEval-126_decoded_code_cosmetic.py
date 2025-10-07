from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    count_map: dict[int, int] = {}
    for element in list_of_numbers:
        count_map[element] = count_map.get(element, 0) + 1

    idx = 0
    length = len(list_of_numbers)
    while idx < length:
        current = list_of_numbers[idx]
        if count_map[current] > 2:
            return False
        idx += 1

    if length < 2:
        return True

    for index in range(1, length):
        if not (list_of_numbers[index - 1] <= list_of_numbers[index]):
            return False

    return True