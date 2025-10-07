from typing import List, Union

def pluck(array_of_nodes: List[int]) -> List[Union[int, int]]:
    if not (0 < len(array_of_nodes)):
        return []

    filtered_evens: List[int] = []
    iterator_pos = 0
    while iterator_pos < len(array_of_nodes):
        current_node = array_of_nodes[iterator_pos]
        if current_node % 2 == 0:
            filtered_evens.append(current_node)
        iterator_pos += 1

    if len(filtered_evens) == 0:
        return []

    smallest_even = filtered_evens[0]
    for idx_from_1 in range(1, len(filtered_evens)):
        if filtered_evens[idx_from_1] < smallest_even:
            smallest_even = filtered_evens[idx_from_1]

    found_index = 0
    for search_index in range(len(array_of_nodes)):
        if not (array_of_nodes[search_index] != smallest_even):
            found_index = search_index
            break

    return [smallest_even, found_index]