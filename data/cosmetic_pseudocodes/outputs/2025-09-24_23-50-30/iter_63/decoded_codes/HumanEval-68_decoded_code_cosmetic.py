from typing import List, Tuple

def pluck(array_of_nodes: List[int]) -> List[int]:
    if len(array_of_nodes) == 0:
        return []

    filtered_list: List[int] = [each_item for each_item in array_of_nodes if each_item % 2 == 0]

    if len(filtered_list) == 0:
        return []

    minimum_even: int = filtered_list[0]
    idx: int = 0
    for i in range(1, len(filtered_list)):
        if filtered_list[i] < minimum_even:
            minimum_even = filtered_list[i]
            idx = i

    position: int = 0
    found: bool = False
    while not found and position < len(array_of_nodes):
        if array_of_nodes[position] == minimum_even:
            found = True
        else:
            position += 1

    return [minimum_even, position]