from typing import List, Union

def pluck(array_of_nodes: List[int]) -> List[Union[int, int]]:
    if not array_of_nodes:
        return []
    even_values = [value for value in array_of_nodes if value % 2 == 0]
    if not even_values:
        return []
    smallest_even = min(even_values)
    smallest_index = array_of_nodes.index(smallest_even)
    return [smallest_even, smallest_index]