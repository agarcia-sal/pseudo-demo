from typing import List

def pluck(array_of_nodes: List[int]) -> List[int]:
    result: List[int] = []
    evens_list: List[int] = []
    i: int = 0

    while i < len(array_of_nodes):
        if array_of_nodes[i] % 2 == 0:
            evens_list.append(array_of_nodes[i])
        i += 1

    if not evens_list:
        return result

    candidate_minimum = evens_list[0]
    for element in evens_list:
        if element < candidate_minimum:
            candidate_minimum = element

    locate_index = 0
    for idx, value in enumerate(array_of_nodes):
        if value == candidate_minimum:
            locate_index = idx
            break

    result = [candidate_minimum, locate_index]
    return result