from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    distinct_vals = set(list_of_integers)
    temp_arr = sorted(distinct_vals)
    arr_len = len(temp_arr)
    if arr_len < 2:
        return None
    return temp_arr[1]