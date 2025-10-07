from typing import List, Union


def pluck(list_nodes: List[int]) -> List[int]:
    if len(list_nodes) == 0:
        return []
    filtered_evens: List[int] = []
    idx_counter = 0
    while idx_counter < len(list_nodes):
        current_item = list_nodes[idx_counter]
        if current_item % 2 == 0:
            filtered_evens.append(current_item)
        idx_counter += 1
    if len(filtered_evens) == 0:
        return []
    min_even = filtered_evens[0]
    idx_min_even = 0
    position_tracker = 1
    while position_tracker < len(filtered_evens):
        if filtered_evens[position_tracker] < min_even:
            min_even = filtered_evens[position_tracker]
            idx_min_even = position_tracker
        position_tracker += 1
    loc_in_original = 0
    while loc_in_original < len(list_nodes):
        if list_nodes[loc_in_original] == min_even:
            break
        loc_in_original += 1
    return [min_even, loc_in_original]