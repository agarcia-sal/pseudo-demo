from typing import List, Union


def f(x: int) -> List[int]:
    x = max(x, 0)  # ensure non-negative input for iteration
    y: int = 1
    z: List[int] = []
    while y <= x:
        if y % 2 == 0:
            a: int = 1
            b: int = 1
            while b <= y:
                a *= b
                b += 1
            z.append(a)
        else:
            c: int = 0
            d: int = 1
            while d <= y:
                c += d
                d += 1
            z.append(c)
        y += 1
    return z