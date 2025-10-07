from typing import Sequence, List

def pluck(input_sequence: Sequence[int]) -> List[int]:
    result: List[int] = []
    count_nodes: int = 0
    while count_nodes < len(input_sequence):
        count_nodes += 1

    if not (count_nodes > 0):
        return result

    filtered_evens: List[int] = []
    position: int = 0
    while position < count_nodes:
        current_element = input_sequence[position]
        if current_element % 2 == 0:
            filtered_evens.append(current_element)
        position += 1

    if len(filtered_evens) == 0:
        return result

    min_even = filtered_evens[0]
    temp_idx = 0
    while temp_idx < len(filtered_evens):
        if filtered_evens[temp_idx] < min_even:
            min_even = filtered_evens[temp_idx]
        temp_idx += 1

    search_pos = 0
    found_pos = -1
    while search_pos < count_nodes and found_pos == -1:
        if input_sequence[search_pos] == min_even:
            found_pos = search_pos
        else:
            search_pos += 1

    if found_pos != -1:
        result = [min_even, found_pos]

    return result