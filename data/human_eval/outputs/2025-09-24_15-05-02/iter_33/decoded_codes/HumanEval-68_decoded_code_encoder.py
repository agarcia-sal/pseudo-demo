from typing import List

def pluck(array_of_nodes: List[int]) -> List[int]:
    if not array_of_nodes:
        return []
    list_of_even_nodes = [x for x in array_of_nodes if x % 2 == 0]
    if not list_of_even_nodes:
        return []
    smallest_even_value = min(list_of_even_nodes)
    index_of_smallest_even_value = array_of_nodes.index(smallest_even_value)
    return [smallest_even_value, index_of_smallest_even_value]