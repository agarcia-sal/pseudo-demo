from typing import Sequence

def add(values_collection: Sequence[int]) -> int:
    total_sum: int = 0
    idx: int = 1
    while idx <= len(values_collection):
        # Adjust index since pseudocode is 1-based, Python is 0-based
        if values_collection[idx - 1] % 2 == 0:
            total_sum += values_collection[idx - 1]
        idx += 2
    return total_sum