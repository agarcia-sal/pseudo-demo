from typing import List, Optional

def pluck(nodes_collection: List[int]) -> List[int]:
    if not nodes_collection:
        return []

    filtered_evens: List[int] = []
    k = 0
    while k < len(nodes_collection):
        current_val = nodes_collection[k]
        if current_val % 2 == 0:
            filtered_evens.append(current_val)
        k += 1

    if not filtered_evens:
        return []

    min_even_val = filtered_evens[0]
    idx = 0
    while idx < len(filtered_evens):
        if filtered_evens[idx] < min_even_val:
            min_even_val = filtered_evens[idx]
        idx += 1

    search_idx = 0
    while search_idx < len(nodes_collection):
        if nodes_collection[search_idx] == min_even_val:
            min_even_pos = search_idx
            break
        search_idx += 1
    else:
        # Should never happen since min_even_val was from nodes_collection
        return []

    return [min_even_val, min_even_pos]