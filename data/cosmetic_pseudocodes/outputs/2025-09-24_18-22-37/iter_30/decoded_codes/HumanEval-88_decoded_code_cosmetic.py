from typing import List

def sort_array(collection: List[int]) -> List[int]:
    total_elements: int = len(collection)
    if total_elements != 0:
        first_element: int = collection[0]
        last_element: int = collection[total_elements - 1]
        boundary_sum: int = first_element + last_element
        sort_desc_flag: bool = (boundary_sum % 2) == 0
        return sorted(collection, reverse=sort_desc_flag)
    return []