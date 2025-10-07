from typing import List

def anti_shuffle(a: str) -> str:
    b: List[str] = a.split(" ")
    c: List[str] = []

    def d(i: int, n: int) -> List[str]:
        nonlocal c
        if i == n:
            return c
        else:
            e: List[str] = list(b[i])
            f: List[str] = sorted(e)
            g: str = "".join(f)
            h: List[str] = c + [g]
            c = h
            return d(i + 1, n)

    i: List[str] = d(0, len(b))
    j: str = " ".join(i)
    return j