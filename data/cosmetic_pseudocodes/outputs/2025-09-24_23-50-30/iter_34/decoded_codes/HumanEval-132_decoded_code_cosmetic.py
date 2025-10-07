from typing import List

def is_nested(a: List[str]) -> bool:
    x: List[int] = []
    y: List[int] = []
    z: int = 0
    w: int = 0
    while z < len(a):
        if a[z] == '[':
            x.append(z)
        else:
            y.append(z)
        z += 1
    y.reverse()
    v: int = len(y)
    for u in x:
        if w < v and u < y[w]:
            # The complex redundant increments/decrements simplify to w += 1
            w += 1
    return w >= 2