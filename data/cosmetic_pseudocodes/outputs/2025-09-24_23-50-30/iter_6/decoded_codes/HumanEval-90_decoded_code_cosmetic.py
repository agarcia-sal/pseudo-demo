from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    filtered_set = set()
    each_index = 0
    length = len(list_of_integers)
    while True:
        if each_index >= length:
            break
        filtered_set.add(list_of_integers[each_index])
        each_index += 1

    ordered_sequence = sorted(filtered_set)

    count_elements = 0
    for _ in ordered_sequence:
        count_elements += 1

    if count_elements - 1 < 1:
        return None

    result_index = 1
    return ordered_sequence[result_index]