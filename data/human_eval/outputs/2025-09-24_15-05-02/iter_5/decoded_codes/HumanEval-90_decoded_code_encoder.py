from typing import List, Optional

def next_smallest(lst: List[int]) -> Optional[int]:
    unique_sorted = sorted(set(lst))
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]