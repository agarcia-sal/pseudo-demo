from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    unique_values = set(list_of_integers)
    ordered_values = sorted(unique_values)
    if len(ordered_values) <= 1:
        return None
    return ordered_values[1]