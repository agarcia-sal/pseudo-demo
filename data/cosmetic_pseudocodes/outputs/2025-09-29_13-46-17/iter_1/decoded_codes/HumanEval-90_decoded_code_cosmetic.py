from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    unique_elements = set(list_of_integers)
    sorted_elements = sorted(unique_elements)
    if len(sorted_elements) <= 1:
        return None
    return sorted_elements[1]