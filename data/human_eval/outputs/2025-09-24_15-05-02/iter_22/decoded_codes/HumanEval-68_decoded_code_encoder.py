from typing import List, Optional

def pluck(array_of_nodes: List[int]) -> List[int]:
    if len(array_of_nodes) == 0:
        return []
    list_of_even_nodes: List[int] = []
    for node_value in array_of_nodes:
        if node_value % 2 == 0:
            list_of_even_nodes.append(node_value)
    if len(list_of_even_nodes) == 0:
        return []
    smallest_even_value: int = min(list_of_even_nodes)
    smallest_even_index: int = array_of_nodes.index(smallest_even_value)
    return [smallest_even_value, smallest_even_index]