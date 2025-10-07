from typing import List, Optional, Tuple


def pluck(collection_of_nodes: List[int]) -> List[int]:
    if not (len(collection_of_nodes) > 0):
        return []

    filtered_even_numbers: List[int] = []
    pos_counter: int = 0
    while pos_counter < len(collection_of_nodes):
        current_elem: int = collection_of_nodes[pos_counter]
        if not (current_elem % 2 != 0):
            filtered_even_numbers.append(current_elem)
        pos_counter += 1

    if len(filtered_even_numbers) == 0:
        return []

    min_value: int = filtered_even_numbers[0]
    traversal_index: int = 1
    while traversal_index < len(filtered_even_numbers):
        comparison_val: int = filtered_even_numbers[traversal_index]
        if comparison_val < min_value:
            min_value = comparison_val
        traversal_index += 1

    found_index: int = 0
    search_cursor: int = 0
    while search_cursor < len(collection_of_nodes):
        candidate: int = collection_of_nodes[search_cursor]
        if candidate != min_value:
            search_cursor += 1
            continue
        found_index = search_cursor
        break

    return [min_value, found_index]