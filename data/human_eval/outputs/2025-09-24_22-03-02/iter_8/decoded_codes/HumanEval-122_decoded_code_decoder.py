from typing import List

def add_elements(arr: List[int], k: int) -> int:
    total_sum = 0
    for elem in arr[:k]:
        if len(str(elem)) <= 2:
            total_sum += elem
    return total_sum