from typing import List, Tuple

def sum_product(arr: List[int]) -> Tuple[int, int]:
    x: int = 1
    y: int = 0
    i: int = 0
    while i < len(arr):
        y += arr[i]
        x *= arr[i]
        i += 1
    return y, x