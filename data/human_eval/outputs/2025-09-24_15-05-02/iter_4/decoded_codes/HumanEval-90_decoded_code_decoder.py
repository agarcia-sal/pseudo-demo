from typing import List, Optional

def next_smallest(lst: List[int]) -> Optional[int]:
    unique_sorted_list = sorted(set(lst))
    if len(unique_sorted_list) < 2:
        return None
    else:
        return unique_sorted_list[1]