from typing import List

def pluck(node_collection: List[int]) -> List[int]:
    count_nodes: int = len(node_collection)
    if count_nodes == 0:
        return []

    filtered_evens: List[int] = []
    iterator: int = 0
    while iterator < count_nodes:
        current_node = node_collection[iterator]
        if current_node % 2 == 0:
            filtered_evens.append(current_node)
        iterator += 1

    count_evens: int = len(filtered_evens)
    if count_evens == 0:
        return []

    minimum_even: int = filtered_evens[0]
    temp_index: int = 0
    iterator = 1
    while iterator < count_evens:
        candidate = filtered_evens[iterator]
        if candidate < minimum_even:
            minimum_even = candidate
            temp_index = iterator
        iterator += 1

    iterator = 0
    index_of_min_even: int = -1
    while iterator < count_nodes:
        if node_collection[iterator] == minimum_even:
            index_of_min_even = iterator
            break
        iterator += 1

    result_list: List[int] = [minimum_even, index_of_min_even]
    return result_list