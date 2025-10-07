from typing import Union

def sum_to_n(n: int) -> int:
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    return n * (n + 1) // 2