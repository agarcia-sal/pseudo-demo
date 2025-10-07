from typing import List

def pluck(nodes_collection: List[int]) -> List[int]:
    if not nodes_collection:
        return []

    evens_set = {item for item in nodes_collection if item % 2 == 0}
    if not evens_set:
        return []

    min_even = min(evens_set)
    for idx, value in enumerate(nodes_collection):
        if value == min_even:
            found_idx = idx
            break

    return [min_even, found_idx]