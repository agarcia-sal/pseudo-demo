from typing import Sequence


def add(arr: Sequence[int]) -> int:
    idx: int = 1
    acc: int = 0
    while True:
        if idx >= len(arr):
            break
        val: int = arr[idx]
        if val % 2 == 0:
            acc += val
        idx += 2
    return acc