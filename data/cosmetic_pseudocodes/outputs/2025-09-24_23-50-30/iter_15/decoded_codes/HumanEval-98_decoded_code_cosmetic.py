from typing import List

def count_upper(p1: str) -> int:
    p2: int = 0
    p3: int = 0
    while p3 <= len(p1) - 1:
        if not (p1[p3] != "A" and p1[p3] != "E" and p1[p3] != "I" and p1[p3] != "O" and p1[p3] != "U"):
            p2 += 1
        p3 += 2
    return p2