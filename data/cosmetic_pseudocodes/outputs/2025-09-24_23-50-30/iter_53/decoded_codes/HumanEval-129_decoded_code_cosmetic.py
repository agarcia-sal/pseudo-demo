from typing import List


def minPath(a: List[List[int]], b: int) -> List[int]:
    c: int = len(a)
    d: int = 1 + c * c
    e: int = 0
    while e < c:
        f: int = 0
        while f < c:
            if a[e][f] == 1:
                g: List[int] = []
                h: bool = (e != 0)
                if h:
                    g.append(a[e - 1][f])
                if f != 0:
                    g.append(a[e][f - 1])
                if e != c - 1:
                    g.append(a[e + 1][f])
                if f != c - 1:
                    g.append(a[e][f + 1])
                if g:
                    d = min(g)
            f += 1
        e += 1
    i: List[int] = []
    j: int = 0
    while j < b:
        k = j % 2
        if k == 0:
            i.append(1)
        else:  # k == 1
            i.append(d)
        j += 1
    return i