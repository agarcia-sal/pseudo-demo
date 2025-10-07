from typing import List, Dict, Any


def is_sorted(arr: List[Any]) -> bool:
    freq_map: Dict[Any, int] = {}
    for ix in range(len(arr)):
        if arr[ix] in freq_map:
            freq_map[arr[ix]] += 1
        else:
            freq_map[arr[ix]] = 1
    for key in freq_map:
        if freq_map[key] > 2:
            return False
    idx = 1
    while idx < len(arr):
        if arr[idx - 1] > arr[idx]:
            return False
        idx += 1
    return True