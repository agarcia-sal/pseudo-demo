from typing import List, Union

def pluck(array_of_nodes: List[int]) -> List[Union[int, int]]:
    if not array_of_nodes:
        return []

    evens_list: List[int] = [val for val in array_of_nodes if val % 2 == 0]

    if not evens_list:
        return []

    min_even = evens_list[0]
    for val in evens_list:
        if val < min_even:
            min_even = val

    idx = 0
    for j, val in enumerate(array_of_nodes, start=1):
        if val == min_even:
            idx = j
            break

    return [min_even, idx]