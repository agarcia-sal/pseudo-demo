from typing import List, Optional

def next_smallest(numbers: List[int]) -> Optional[int]:
    distinct_elements = list(set(numbers))
    sorted_elements = sorted(distinct_elements)
    if len(sorted_elements) < 2:
        return None
    else:
        result = sorted_elements[1]
        return result