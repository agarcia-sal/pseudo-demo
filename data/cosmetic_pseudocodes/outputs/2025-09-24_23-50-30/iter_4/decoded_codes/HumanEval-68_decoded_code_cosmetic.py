from typing import List, Optional, Union


def pluck(array_of_nodes: List[int]) -> List[Union[int, int]]:
    def find_minimum(elems: List[int], current_min: int, index: int) -> int:
        if index == len(elems):
            return current_min
        else:
            next_min = elems[index] if elems[index] < current_min else current_min
            return find_minimum(elems, next_min, index + 1)

    def locate_index(collection: List[int], target: int, pos: int) -> int:
        if pos == len(collection):
            return -1
        elif collection[pos] == target:
            return pos
        else:
            return locate_index(collection, target, pos + 1)

    if not array_of_nodes:
        return []

    even_filtered = [node for node in array_of_nodes if node % 2 == 0]

    if not even_filtered:
        return []

    minimum_even = find_minimum(even_filtered, even_filtered[0], 1)
    position = locate_index(array_of_nodes, minimum_even, 0)
    return [minimum_even, position]