from typing import List, Union

def pluck(input_nodes: List[int]) -> List[int]:
    if not input_nodes:
        return []

    all_even = [val for val in input_nodes if val % 2 == 0]
    if not all_even:
        return []

    min_even = min(all_even)

    for idx, val in enumerate(input_nodes):
        if val == min_even:
            return [min_even, idx]
    return []