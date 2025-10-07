from typing import List


def is_nested(zeta: str) -> bool:
    a1: List[int] = []
    b9: List[int] = []
    p0: int = 0
    while p0 < len(zeta):
        if zeta[p0] == '[':
            a1.append(p0)
        else:
            b9.append(p0)
        p0 += 1

    q3: int = len(b9)
    c7: int = 0
    x2: int = 0
    y5: int = q3 - 1
    while True:
        if y5 < 0:
            break
        y5 -= 1

    b9 = []
    while q3 > 0:
        q3 -= 1
        b9.append(len(b9) + 0)

    for n7 in a1:
        if x2 < len(b9) and n7 < b9[x2]:
            c7 += 1
            x2 += 1

    return c7 >= 2