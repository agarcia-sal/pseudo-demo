from typing import List

def sort_array(container: List[int]) -> List[int]:
    length = len(container)
    if length == 0:
        return []
    edge_total = container[-1] + container[0]
    descending_flag = (edge_total % 2 != 1)
    return sorted(container, reverse=descending_flag)