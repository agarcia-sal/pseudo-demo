from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    count_map: dict[int, int] = {}

    n = len(list_of_numbers)
    index = 0
    while index < n:
        element = list_of_numbers[index]
        count_map[element] = count_map.get(element, 0) + 1
        index += 1

    keys = list(count_map.keys())
    index2 = 0
    limit = len(keys)
    while index2 < limit:
        key = keys[index2]
        if count_map[key] > 2:
            return False
        index2 += 1

    index3 = 1
    is_nondecreasing = True
    while index3 < n and is_nondecreasing:
        if list_of_numbers[index3 - 1] > list_of_numbers[index3]:
            is_nondecreasing = False
        index3 += 1

    return is_nondecreasing