from typing import Sequence

def add_elements(arr: Sequence[int], k: int) -> int:
    total_sum: int = 0
    for element in arr[:k]:
        if len(str(element)) <= 2:
            total_sum += element
    return total_sum