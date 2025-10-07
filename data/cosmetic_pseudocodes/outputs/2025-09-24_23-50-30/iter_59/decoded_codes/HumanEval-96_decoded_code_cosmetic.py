from typing import List

def count_up_to(w: int) -> List[int]:
    u: List[int] = []
    v: int = 2
    while True:
        if not (v < w):
            break
        x: bool = True
        y: int = 2
        while True:
            if not (y < v):
                break
            if not (v % y != 0):  # If v % y == 0
                x = False
                break
            y += 1
        if x:
            u.append(v)
        v += 1
    return u