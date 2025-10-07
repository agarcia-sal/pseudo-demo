from typing import Sequence

def add(arr: Sequence[int]) -> int:
    totalSum: int = 0
    idx: int = 1
    while idx <= len(arr):
        elt: int = arr[idx - 1]  # pseudocode arrays are 1-based; Python 0-based
        if elt % 2 == 0:
            totalSum += elt
        idx += 2
    return totalSum