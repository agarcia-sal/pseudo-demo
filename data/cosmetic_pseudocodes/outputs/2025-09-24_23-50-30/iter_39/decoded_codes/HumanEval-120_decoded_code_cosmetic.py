from typing import List, Union

def maximum(w: List[int], x: int) -> List[int]:
    if x == 0:
        return []
    w_sorted = sorted(w)
    y = len(w_sorted) - x
    z: List[int] = []
    while y < len(w_sorted):
        z.append(w_sorted[y])
        y += 1
    return z