from typing import List, Optional

def can_arrange(array: List[int]) -> Optional[int]:
    iter_var: int = 1
    pos_marker: Optional[int] = None
    while iter_var < len(array):
        if not (array[iter_var - 1] <= array[iter_var]):
            pos_marker = iter_var
        iter_var += 1
    return pos_marker