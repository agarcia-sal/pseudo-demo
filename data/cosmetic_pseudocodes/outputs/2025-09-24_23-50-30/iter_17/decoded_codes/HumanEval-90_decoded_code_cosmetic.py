from typing import List, Optional

def next_smallest(array_of_numbers: List[int]) -> Optional[int]:
    distinct_collection = {element: True for element in array_of_numbers}
    ordered_keys = list(distinct_collection.keys())
    n = len(ordered_keys)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if ordered_keys[j] > ordered_keys[j + 1]:
                ordered_keys[j], ordered_keys[j + 1] = ordered_keys[j + 1], ordered_keys[j]
    if n < 2:
        return None
    return ordered_keys[1]