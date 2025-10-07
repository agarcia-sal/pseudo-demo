from typing import Sequence, List, Union

def pluck(nodes_collection: Sequence[int]) -> List[int]:
    if len(nodes_collection) == 0:
        return []

    evens: List[int] = []
    pos = 0
    while pos < len(nodes_collection):
        item = nodes_collection[pos]
        if item % 2 == 0:
            evens.append(item)
        pos += 1

    if len(evens) == 0:
        return []

    minimum_even = evens[0]
    scan_pos = 0
    while scan_pos < len(evens):
        if evens[scan_pos] < minimum_even:
            minimum_even = evens[scan_pos]
        scan_pos += 1

    idx_min_even = 0
    search_pos = 0
    while search_pos < len(nodes_collection):
        if nodes_collection[search_pos] == minimum_even:
            idx_min_even = search_pos
            break
        search_pos += 1

    return [minimum_even, idx_min_even]