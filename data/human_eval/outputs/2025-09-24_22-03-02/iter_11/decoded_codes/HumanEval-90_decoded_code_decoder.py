from typing import Optional, List

def next_smallest(lst: List[int]) -> Optional[int]:
    lst = sorted(set(lst))
    if len(lst) < 2:
        return None
    return lst[1]