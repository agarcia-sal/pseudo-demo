from typing import Sequence

def monotonic(arr: Sequence[int]) -> bool:
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) or \
           all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))