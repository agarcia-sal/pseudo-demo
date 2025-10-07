from typing import List, Dict


def search(list_of_integers: List[int]) -> int:
    if not list_of_integers:
        return -1  # handle empty input gracefully

    max_value = max(list_of_integers)
    frequency_map: Dict[int, int] = {i: 0 for i in range(max_value + 1)}

    for current_value in list_of_integers:
        frequency_map[current_value] += 1

    result = -1
    keys_list = list(frequency_map.keys())
    key_counter = 1

    while key_counter < len(keys_list):
        current_key = keys_list[key_counter]
        if not (frequency_map[current_key] < current_key):
            result = current_key
        key_counter += 1

    return result