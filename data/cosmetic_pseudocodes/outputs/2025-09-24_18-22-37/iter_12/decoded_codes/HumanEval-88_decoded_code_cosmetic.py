from typing import List

def sort_array(collection: List[int]) -> List[int]:
    if len(collection) < 1:
        return []
    initial_element: int = collection[0]
    final_element: int = collection[-1]
    sum_edge_values: int = initial_element + final_element
    descending_flag: bool = (sum_edge_values % 2 == 0)
    return sorted(collection, reverse=descending_flag)