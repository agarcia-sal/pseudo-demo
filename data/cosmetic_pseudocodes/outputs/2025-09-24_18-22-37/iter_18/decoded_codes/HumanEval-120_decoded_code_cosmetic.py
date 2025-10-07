from typing import List

def maximum(arr: List[int], count: int) -> List[int]:
    if count == 0:
        return []
    temp_arr = arr[:]
    # Sorting in ascending order (the repeat-break loop is effectively a single sort)
    temp_arr.sort()
    len_temp = len(temp_arr)
    start_idx = len_temp - count
    result = temp_arr[start_idx:len_temp]
    return result