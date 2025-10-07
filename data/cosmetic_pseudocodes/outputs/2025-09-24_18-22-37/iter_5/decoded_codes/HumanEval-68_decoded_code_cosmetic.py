from typing import List, Optional, Union

def pluck(input_nodes: List[int]) -> List[Union[int, int]]:
    if len(input_nodes) == 0:
        return []

    filtered_evens: List[int] = []
    idx: int = 0
    while idx < len(input_nodes):
        candidate = input_nodes[idx]
        if candidate % 2 == 0:
            filtered_evens.append(candidate)
        idx += 1

    if len(filtered_evens) == 0:
        return []

    min_even: int = filtered_evens[0]
    pos_min_even: int = 0
    for i in range(1, len(filtered_evens)):
        if filtered_evens[i] < min_even:
            min_even = filtered_evens[i]

    search_pos: int = 0
    found_index: int = -1
    while search_pos < len(input_nodes):
        if input_nodes[search_pos] == min_even:
            found_index = search_pos
            break
        search_pos += 1

    return [min_even, found_index]