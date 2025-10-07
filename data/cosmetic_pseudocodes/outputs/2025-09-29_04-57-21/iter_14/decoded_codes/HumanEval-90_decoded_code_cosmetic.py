from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    distinct_values: List[int] = []
    index_counter: int = 0

    while index_counter < len(list_of_integers):
        if list_of_integers[index_counter] not in distinct_values:
            distinct_values.append(list_of_integers[index_counter])
        index_counter += 1

    sorted_values: List[int] = distinct_values
    i: int = 0
    # Bubble sort variant to sort values ascendingly
    while i < len(sorted_values) - 1:
        if sorted_values[i] > sorted_values[i + 1]:
            sorted_values[i], sorted_values[i + 1] = sorted_values[i + 1], sorted_values[i]
            i = -1  # reset to start after swap
        i += 1

    if len(sorted_values) < 2:
        return None

    return sorted_values[1]