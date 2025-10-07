from typing import List


def sort_array(collection: List[int]) -> List[int]:
    if not collection:
        return []
    boundary_sum = collection[0] + collection[-1]
    descending_flag = (boundary_sum % 2) == 0
    return sorted(collection, reverse=descending_flag)