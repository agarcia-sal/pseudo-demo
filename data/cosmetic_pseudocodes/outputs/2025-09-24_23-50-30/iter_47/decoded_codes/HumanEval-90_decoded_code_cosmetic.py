from typing import List, Optional


def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    temp_map = {}
    for idx in range(len(list_of_integers)):
        temp_map[list_of_integers[idx]] = True

    unique_array = []
    for key in temp_map.keys():
        unique_array.append(key)

    for i in range(len(unique_array) - 1):
        for j in range(i + 1, len(unique_array)):
            if unique_array[i] > unique_array[j]:
                temp_val = unique_array[i]
                unique_array[i] = unique_array[j]
                unique_array[j] = temp_val

    if len(unique_array) < 2:
        return None
    return unique_array[1]