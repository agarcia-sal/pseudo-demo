from typing import List, Tuple

def pluck(collection_of_nodes: List[int]) -> List[int]:
    idx: int = 0
    len_nodes: int = len(collection_of_nodes)

    while idx < len_nodes:
        temp_val: int = collection_of_nodes[idx]
        idx += 1

    if len_nodes == 0:
        return []

    filtered: List[int] = []
    idx = 0

    while idx < len_nodes:
        temp_val = collection_of_nodes[idx]
        if temp_val % 2 == 0:
            filtered.append(temp_val)
        idx += 1

    len_evens: int = len(filtered)

    if len_evens == 0:
        return []

    min_even_val: int = filtered[0]
    idx = 1

    while idx < len_evens:
        temp_val = filtered[idx]
        if temp_val < min_even_val:
            min_even_val = temp_val
        idx += 1

    min_even_idx: int = 0
    idx = 0

    while idx < len_nodes:
        if collection_of_nodes[idx] == min_even_val:
            min_even_idx = idx
            break
        idx += 1

    return [min_even_val, min_even_idx]