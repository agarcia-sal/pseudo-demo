from typing import List, Union

def pluck(array_of_nodes: List[int]) -> List[int]:
    if len(array_of_nodes) == 0:
        return []
    even_nodes = [node for node in array_of_nodes if node % 2 == 0]
    if not even_nodes:
        return []
    smallest_even = min(even_nodes)
    smallest_index = array_of_nodes.index(smallest_even)
    return [smallest_even, smallest_index]