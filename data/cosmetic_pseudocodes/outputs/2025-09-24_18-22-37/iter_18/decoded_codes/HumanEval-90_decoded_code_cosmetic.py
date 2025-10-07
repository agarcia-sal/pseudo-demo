from typing import List, Optional

def next_smallest(arr_values: List[int]) -> Optional[int]:
    temp_set = set()
    idx_counter = 0
    while idx_counter < len(arr_values):
        if arr_values[idx_counter] not in temp_set:
            temp_set.add(arr_values[idx_counter])
        idx_counter += 1

    ordered_unique = sorted(temp_set)
    if len(ordered_unique) < 2:
        return None

    # The REPEAT...RETURN ordered_unique.at(1) UNTIL TRUE is equivalent to returning the second smallest element.
    return ordered_unique[1]