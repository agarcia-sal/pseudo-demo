from typing import List

def sort_array(collection: List[int]) -> List[int]:
    if not collection:
        return []
    boundary_sum = collection[-1] + collection[0]
    descending_flag = (boundary_sum % 2) == 0
    return sorted(collection, reverse=descending_flag)