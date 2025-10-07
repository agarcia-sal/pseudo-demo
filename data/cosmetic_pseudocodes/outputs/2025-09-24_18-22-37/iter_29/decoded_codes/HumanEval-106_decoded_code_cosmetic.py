from typing import List

def f(q: int) -> List[int]:
    X: List[int] = []
    u: int = 1
    while u <= q:
        if u % 2 == 0:
            k: int = 1
            y: int = 1
            while y <= u:
                k *= y
                y += 1
            X.append(k)
        else:
            p: int = 0
            r: int = 1
            while r <= u:
                p += r
                r += 1
            X.append(p)
        u += 1
    return X