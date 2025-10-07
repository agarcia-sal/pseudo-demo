from typing import List

def maximum(arr: List[int], k: int) -> List[int]:
    if k == 0:
        return []
    if k < 0:
        # Negative k is invalid; return empty list to handle robustly
        return []
    if k > len(arr):
        # If k is greater than length of arr, return entire sorted arr
        k = len(arr)
    arr_sorted = sorted(arr)
    ans = arr_sorted[len(arr_sorted) - k:]
    return ans