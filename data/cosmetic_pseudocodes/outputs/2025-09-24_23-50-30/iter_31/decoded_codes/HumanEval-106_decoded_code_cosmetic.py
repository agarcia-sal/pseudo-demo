from typing import List

def f(x: int) -> List[int]:
    y: List[int] = []
    for w in range(1, x + 1):
        if w % 2 == 0:
            z: int = 1
            a: int = 1
            while a <= w:
                z *= a
                a += 1
            y.append(z)
        else:
            b: int = 0
            c: int = 1
            while c <= w:
                b += c
                c += 1
            y.append(b)
    return y