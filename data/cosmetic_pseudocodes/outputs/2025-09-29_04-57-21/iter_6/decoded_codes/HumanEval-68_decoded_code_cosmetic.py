from typing import List, Optional

def pluck(array_of_nodes: List[int]) -> List[int]:
    if not array_of_nodes:
        return []

    filtered_list = [item for item in array_of_nodes if item % 2 == 0]

    if not filtered_list:
        return []

    minimum_even = filtered_list[0]
    for val in filtered_list:
        if val < minimum_even:
            minimum_even = val

    position = 0
    for index, value in enumerate(array_of_nodes):
        if value == minimum_even:
            position = index
            break

    return [minimum_even, position]