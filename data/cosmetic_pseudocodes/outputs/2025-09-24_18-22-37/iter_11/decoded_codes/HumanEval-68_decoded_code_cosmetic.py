from typing import List, Optional


def pluck(nodes_collection: List[int]) -> List[int]:
    node_count: int = len(nodes_collection)
    collected_evens: List[int] = []

    # Collect even numbers from nodes_collection
    for temp_value in nodes_collection:
        if temp_value % 2 == 0:
            collected_evens.append(temp_value)

    if node_count == 0 or not collected_evens:
        return []

    min_even: int = collected_evens[0]
    for temp_value in collected_evens[1:]:
        if temp_value < min_even:
            min_even = temp_value

    min_even_index: int = 0
    # Find index of min_even in nodes_collection
    while min_even_index < node_count and nodes_collection[min_even_index] != min_even:
        min_even_index += 1

    return [min_even, min_even_index]