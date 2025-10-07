from typing import List, Optional

def pluck(array_of_nodes: List[int]) -> List[int]:
    if not array_of_nodes:
        return []
    evens = [item for item in array_of_nodes if item % 2 == 0]
    if not evens:
        return []
    min_even = evens[0]
    for val in evens:
        if val < min_even:
            min_even = val
    for i, val in enumerate(array_of_nodes):
        if val == min_even:
            return [min_even, i]
    # Fallback (should not reach here if min_even was found)
    return []