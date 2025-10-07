from typing import List


def digits(x: int) -> int:
    u: int = 1
    v: int = 0
    w: List[str] = list(str(x))
    i: int = 0

    while i < len(w):
        y: int = int(w[i])
        if y % 2 == 1:
            u *= y
            v += 1
        i += 1

    if v == 0:
        return 0
    else:
        return u