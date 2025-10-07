from typing import Sequence

def monotonic(arr: Sequence[int]) -> bool:
    ascending_check = list(arr) == sorted(arr)
    descending_check = list(arr) == sorted(arr, reverse=True)
    return ascending_check or descending_check