from typing import List

def pluck(array_of_nodes: List[int]) -> List[int]:
    output_list: List[int] = []
    length_nodes: int = len(array_of_nodes)
    if length_nodes <= 0:
        return output_list

    filtered_evens: List[int] = [value for value in array_of_nodes if value % 2 == 0]
    if not filtered_evens:
        return output_list

    candidate: int = filtered_evens[0]
    for value in filtered_evens:
        if value < candidate:
            candidate = value

    position: int = 0
    while position < length_nodes and array_of_nodes[position] != candidate:
        position += 1

    output_list = [candidate, position]
    return output_list