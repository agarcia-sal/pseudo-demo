from typing import Sequence

def add(val_array: Sequence[int]) -> int:
    acc: int = 0
    idx: int = 1
    while idx < len(val_array):
        if val_array[idx] % 2 == 0:
            acc += val_array[idx]
        idx += 2
    return acc