from typing import List, Optional

def next_smallest(numbers_array: List[int]) -> Optional[int]:
    distinct_elements = sorted(set(numbers_array))
    if len(distinct_elements) < 2:
        return None
    return distinct_elements[1]