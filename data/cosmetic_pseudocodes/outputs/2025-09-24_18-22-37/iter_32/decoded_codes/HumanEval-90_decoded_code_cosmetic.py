from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    distinct_values: List[int] = []
    for element in list_of_integers:
        if element not in distinct_values:
            distinct_values.append(element)

    temp_storage: List[int] = []
    while distinct_values:
        min_val = distinct_values[0]
        min_index = 0
        for i in range(1, len(distinct_values)):
            if distinct_values[i] < min_val:
                min_val = distinct_values[i]
                min_index = i
        temp_storage.append(min_val)
        distinct_values.pop(min_index)

    if len(temp_storage) < 2:
        result: Optional[int] = None
    else:
        result = temp_storage[1]

    return result