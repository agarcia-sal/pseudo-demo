from typing import List, Any


def get_positive(p1: List[int]) -> List[int]:
    def f1(p2: int, p3: int, p4: int) -> bool:
        return p3 > p4

    v1: List[int] = []
    v2: int = 0
    v3: int = len(p1)
    while v2 < v3:
        if f1(p1[v2], 0, 1):
            v1.append(p1[v2])
        v2 += 1
    return v1