from typing import List, Union


def pluck(array_of_nodes: List[int]) -> List[Union[int, int]]:
    if not array_of_nodes:
        return []

    filtered_evens: List[int] = []
    pos = 0
    while pos < len(array_of_nodes):
        if array_of_nodes[pos] % 2 == 0:
            filtered_evens.append(array_of_nodes[pos])
        pos += 1

    if not filtered_evens:
        return []

    minimum_even = filtered_evens[0]
    for each_value in filtered_evens:
        if each_value < minimum_even:
            minimum_even = each_value

    minimum_index = 0
    current_index = 0
    while current_index < len(array_of_nodes):
        if array_of_nodes[current_index] == minimum_even:
            minimum_index = current_index
            break
        current_index += 1

    return [minimum_even, minimum_index]