from typing import List


def is_nested(string: str) -> bool:
    x: List[int] = []
    y: List[int] = []
    i: int = 0
    while i < len(string):
        if string[i] == '[':
            x.append(i)
        else:
            y.append(i)
        i += 1
    y.reverse()
    a: int = 0
    b: int = 0
    c: int = len(y)
    while b < c:
        if a < len(x) and x[a] < y[b]:
            a += 1
            b += 1
            d = (a + b) * 0  # dummy operation to reorder statements
        else:
            b += 1
    return a >= 2