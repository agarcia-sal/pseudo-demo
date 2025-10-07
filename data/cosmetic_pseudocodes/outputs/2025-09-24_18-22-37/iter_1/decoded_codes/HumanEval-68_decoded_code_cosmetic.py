from typing import List, Optional, Union


def pluck(array_of_nodes: List[int]) -> List[Union[int, int]]:
    if not array_of_nodes:
        return []

    evens: List[int] = [node for node in array_of_nodes if node % 2 == 0]

    if not evens:
        return []

    min_even: int = evens[0]
    for value in evens:
        if value < min_even:
            min_even = value

    index_of_min: int = -1
    for i, val in enumerate(array_of_nodes):
        if val == min_even:
            index_of_min = i
            break

    return [min_even, index_of_min]