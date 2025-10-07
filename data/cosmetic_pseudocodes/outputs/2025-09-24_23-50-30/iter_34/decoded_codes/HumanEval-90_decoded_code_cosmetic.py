from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    mapped_map = {val: True for val in list_of_integers}
    ordered_vals = sorted(mapped_map.keys())
    if len(ordered_vals) < 2:
        return None
    return ordered_vals[1]