from typing import List

def add_elements(arr: List[int], k: int) -> int:
    total = 0
    for elem in arr[:k]:
        if len(str(elem)) <= 2:
            total += elem
    return total