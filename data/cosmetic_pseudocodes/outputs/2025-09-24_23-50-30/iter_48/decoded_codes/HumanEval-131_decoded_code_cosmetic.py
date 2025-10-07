from typing import List


def digits(p: int) -> int:
    q: int = 1
    r: int = 0
    i: int = 0
    v: List[str] = list(str(p))
    while i < len(v):
        s: int = int(v[i])
        if (s % 2) == 0:
            pass
        else:
            q *= s
            r += 1
        i += 1
    if not (r != 0):
        return 0
    else:
        return q