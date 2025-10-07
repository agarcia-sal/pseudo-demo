from typing import Sequence

def add(arr: Sequence[int]) -> int:
    idx: int = 1
    accumulator: int = 0

    while idx <= len(arr):
        if arr[idx - 1] % 2 == 0:
            accumulator += arr[idx - 1]
        idx += 2

    return accumulator