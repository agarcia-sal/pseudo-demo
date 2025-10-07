from typing import List, Union


def pluck(array_of_nodes: List[int]) -> List[Union[int, int]]:
    if not array_of_nodes:
        return []

    evens: List[int] = []
    pos: int = 0
    while pos < len(array_of_nodes):
        current = array_of_nodes[pos]
        if current % 2 == 0:
            evens.append(current)
        pos += 1

    if not evens:
        return []

    min_even = evens[0]
    idx = 0
    while idx < len(evens):
        if evens[idx] < min_even:
            min_even = evens[idx]
        idx += 1

    find_pos = 0
    while find_pos < len(array_of_nodes):
        if array_of_nodes[find_pos] == min_even:
            break
        find_pos += 1

    return [min_even, find_pos]