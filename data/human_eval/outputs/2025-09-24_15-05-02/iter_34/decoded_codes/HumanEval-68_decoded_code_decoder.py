from typing import List, Optional, Union

def pluck(array_of_nodes: List[int]) -> List[int]:
    if not array_of_nodes:
        return []
    even_values = [x for x in array_of_nodes if x % 2 == 0]
    if not even_values:
        return []
    smallest_even_value = min(even_values)
    smallest_even_index = array_of_nodes.index(smallest_even_value)
    return [smallest_even_value, smallest_even_index]