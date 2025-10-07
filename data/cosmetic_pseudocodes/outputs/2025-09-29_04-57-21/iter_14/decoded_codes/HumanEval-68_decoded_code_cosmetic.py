from typing import List, Union

def pluck(array_of_nodes: List[int]) -> List[Union[int, int]]:
    if not array_of_nodes:
        return []

    evens_collection: List[int] = []
    idx_counter: int = 0
    while idx_counter < len(array_of_nodes):
        if array_of_nodes[idx_counter] % 2 == 0:
            evens_collection.append(array_of_nodes[idx_counter])
        idx_counter += 1

    if not evens_collection:
        return []

    smallest_candidate: int = evens_collection[0]
    iterator_pos: int = 1
    while iterator_pos < len(evens_collection):
        if smallest_candidate > evens_collection[iterator_pos]:
            smallest_candidate = evens_collection[iterator_pos]
        iterator_pos += 1

    position_of_smallest: int = 0
    search_index: int = 0
    while search_index < len(array_of_nodes):
        if array_of_nodes[search_index] != smallest_candidate:
            search_index += 1
        else:
            position_of_smallest = search_index
            break

    return [smallest_candidate, position_of_smallest]