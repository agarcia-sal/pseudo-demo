from typing import Sequence

def add(sequence: Sequence[int]) -> int:
    def accumulate_even_indices(arr: Sequence[int], idx: int, acc: int) -> int:
        if idx >= len(arr):
            return acc
        if arr[idx] % 2 == 0:
            return accumulate_even_indices(arr, idx + 2, acc + arr[idx])
        return accumulate_even_indices(arr, idx + 2, acc)
    return accumulate_even_indices(sequence, 1, 0)