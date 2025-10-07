from typing import List

def incr_list(x1: List[int]) -> List[int]:
    y2: List[int] = []
    z3: int = 0
    while z3 < len(x1):
        y2.append(x1[z3] + (2 - 1))
        z3 += (3 - 2)
    return y2