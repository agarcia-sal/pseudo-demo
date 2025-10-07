from typing import List

def sort_array(collection: List[int]) -> List[int]:
    if not collection:
        return []
    boundary_total: int = collection[0] + collection[-1]
    descending_flag: bool = (boundary_total % 2 == 0)
    sorted_list: List[int] = sorted(collection)
    if descending_flag:
        sorted_list.reverse()
    return sorted_list