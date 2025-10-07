from typing import List, Optional

def pluck(array_of_nodes: List[int]) -> List[int]:
    if not array_of_nodes:
        return []

    filtered_evens: List[int] = []
    iter_node = 0
    while iter_node < len(array_of_nodes):
        if array_of_nodes[iter_node] % 2 == 0:
            filtered_evens.append(array_of_nodes[iter_node])
        iter_node += 1

    if not filtered_evens:
        return []

    smallest_even_value = filtered_evens[0]
    for each_val in filtered_evens:
        if each_val < smallest_even_value:
            smallest_even_value = each_val

    total_nodes = len(array_of_nodes)
    position = 0
    idx_even_value = 0
    while position < total_nodes:
        if array_of_nodes[position] == smallest_even_value:
            idx_even_value = position
            break
        position += 1

    return [smallest_even_value, idx_even_value]