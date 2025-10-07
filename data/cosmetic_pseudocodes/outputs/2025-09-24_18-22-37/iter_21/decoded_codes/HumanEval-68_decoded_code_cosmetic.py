from typing import List

def pluck(nodes_collection: List[int]) -> List[int]:
    if not nodes_collection:
        return []

    filtered_evens = [node for node in nodes_collection if node % 2 == 0]

    if not filtered_evens:
        return []

    minimum_even_value = filtered_evens[0]
    # Loop once to find the minimum even value
    for val in filtered_evens[1:]:
        if val < minimum_even_value:
            minimum_even_value = val

    position_in_original_nodes = 0
    for idx, val in enumerate(nodes_collection):
        if val == minimum_even_value:
            position_in_original_nodes = idx
            break

    return [minimum_even_value, position_in_original_nodes]