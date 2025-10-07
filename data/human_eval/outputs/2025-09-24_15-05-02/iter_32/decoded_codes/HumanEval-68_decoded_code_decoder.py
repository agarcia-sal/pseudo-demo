from typing import List, Union


def pluck(array_of_nodes: List[int]) -> List[Union[int, int]]:
    if not array_of_nodes:
        return []
    list_of_even_nodes = [element for element in array_of_nodes if element % 2 == 0]
    if not list_of_even_nodes:
        return []
    smallest_even_value = min(list_of_even_nodes)
    index_of_smallest_even_value = array_of_nodes.index(smallest_even_value)
    return [smallest_even_value, index_of_smallest_even_value]