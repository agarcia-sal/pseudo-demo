from typing import List

def sort_array(u: List[int]) -> List[int]:
    if not len(u) > 0:
        return []
    w = u[-1] + u[0]
    v = w - 2 * (w // 2) == 0  # True if w is even, False if odd
    return sorted(u, reverse=v)