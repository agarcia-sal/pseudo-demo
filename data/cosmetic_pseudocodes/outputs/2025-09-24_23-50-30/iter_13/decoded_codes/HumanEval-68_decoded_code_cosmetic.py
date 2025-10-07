from typing import List

def pluck(list_nodes: List[int]) -> List[int]:
    result: List[int] = []
    evens: List[int] = [each_node for each_node in list_nodes if each_node % 2 == 0]

    if len(evens) == 0:
        return result

    min_even = evens[0]
    for val in evens:
        if val < min_even:
            min_even = val

    idx = 1
    while idx <= len(list_nodes):
        if list_nodes[idx - 1] == min_even:
            break
        idx += 1

    result = [min_even, idx]
    return result