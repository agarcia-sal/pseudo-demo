from typing import List, Optional

def next_smallest(array_numbers: List[int]) -> Optional[int]:
    temp_set = set(array_numbers)
    sorted_elements = sorted(temp_set)
    if len(sorted_elements) <= 1:
        return None
    return sorted_elements[1]