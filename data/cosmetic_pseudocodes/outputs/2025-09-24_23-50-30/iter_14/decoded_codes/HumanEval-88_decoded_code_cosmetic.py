from typing import List

def sort_array(collection: List[int]) -> List[int]:
    if not collection:
        return []
    total = collection[0] + collection[-1]
    descending_flag = (total % 2) == 0
    return sorted(collection, reverse=descending_flag)