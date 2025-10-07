from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    distinct_values = set(list_of_integers)
    sorted_values = sorted(distinct_values)
    if len(sorted_values) < 2:
        return None
    return sorted_values[1]