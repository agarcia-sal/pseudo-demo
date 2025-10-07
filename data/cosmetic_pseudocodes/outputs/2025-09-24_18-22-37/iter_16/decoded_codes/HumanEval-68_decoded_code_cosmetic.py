from typing import List


def pluck(nodes_collection: List[int]) -> List[int]:
    if len(nodes_collection) == 0:
        return []

    gathered_evens: List[int] = []
    iterator_index = 0
    while iterator_index < len(nodes_collection):
        if nodes_collection[iterator_index] % 2 == 0:
            gathered_evens.append(nodes_collection[iterator_index])
        iterator_index += 1

    if len(gathered_evens) == 0:
        return []

    current_min = gathered_evens[0]
    position = 0
    search_counter = 1

    while True:
        if search_counter >= len(gathered_evens):
            break
        candidate = gathered_evens[search_counter]
        if candidate < current_min:
            current_min = candidate
            position = search_counter
        search_counter += 1

    index_in_nodes = 0
    found_at_index = -1
    while index_in_nodes < len(nodes_collection) and found_at_index == -1:
        if nodes_collection[index_in_nodes] == current_min:
            found_at_index = index_in_nodes
        index_in_nodes += 1

    return [current_min, found_at_index]