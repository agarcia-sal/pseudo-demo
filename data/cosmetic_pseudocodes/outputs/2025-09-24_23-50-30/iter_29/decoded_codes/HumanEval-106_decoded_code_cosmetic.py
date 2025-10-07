from typing import List

def f(x: int) -> List[int]:
    w: List[int] = []
    y: int = 1
    while y <= x:
        if (y % 2) == 0:
            z: int = 1
            a: int = 1
            while a <= y:
                z *= a
                a += 1
            w.append(z)
        else:
            b: int = 0
            c: int = 1
            while c <= y:
                b += c
                c += 1
            w.append(b)
        y += 1
    return w