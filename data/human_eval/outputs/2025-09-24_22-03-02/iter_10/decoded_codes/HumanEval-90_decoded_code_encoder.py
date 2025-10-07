from typing import List, Optional

def next_smallest(lst: List[int]) -> Optional[int]:
    lst = sorted(set(lst))
    if len(lst) < 2:
        return None
    else:
        return lst[1]