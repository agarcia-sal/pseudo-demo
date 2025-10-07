from typing import List, Union

def pluck(array_of_nodes: List[int]) -> List[Union[int, int]]:
    if not array_of_nodes:
        return []

    evens = [item for item in array_of_nodes if item % 2 == 0]
    if not evens:
        return []

    min_even = min(evens)
    position = next(i for i, val in enumerate(array_of_nodes) if val == min_even)

    return [min_even, position]