from typing import List, Any


def sort_even(a0: List[Any]) -> List[Any]:
    b1: List[Any] = []
    c2: List[Any] = []
    d3: int = 0
    while d3 < len(a0):
        if d3 % 2 == 0:
            b1.append(a0[d3])
        else:
            c2.append(a0[d3])
        d3 += 1
    b1.sort()
    e4: List[Any] = []
    f5: int = 0
    while f5 < len(c2) and f5 < len(b1):
        e4.append(b1[f5])
        e4.append(c2[f5])
        f5 += 1
    if len(b1) > len(c2):
        e4.append(b1[len(b1) - 1])
    return e4