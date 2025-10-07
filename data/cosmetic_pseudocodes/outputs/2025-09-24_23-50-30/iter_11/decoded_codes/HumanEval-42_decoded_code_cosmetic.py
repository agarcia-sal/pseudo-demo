from typing import List

def incr_list(x: List[int]) -> List[int]:
    y: List[int] = []
    z: int = 0
    while z < len(x):
        y.append(x[z] + 1)
        z += 1
    return y