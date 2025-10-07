from typing import List

def anti_shuffle(x: List[str]) -> str:
    y: List[str] = []
    z: int = 0
    while z < len(x):
        a: str = x[z]
        b: List[str] = sorted(list(a))
        c: str = "".join(b)
        y.append(c)
        z += 1
    e: str = ""
    f: int = 0
    while f < len(y):
        e += y[f]
        if f < len(y) - 1:
            e += " "
        f += 1
    return e