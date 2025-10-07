from typing import List

def f(x: int) -> List[int]:
    y: List[int] = []
    a: int = 1
    while a <= x:
        r: int = a % 2
        if r != 1:
            b: int = 1
            c: int = 1
            while c <= a:
                b *= c
                c += 1
            y.append(b)
        else:
            d: int = 0
            e: int = 1
            while e <= a:
                d += e
                e += 1
            y.append(d)
        a += 1
    return y