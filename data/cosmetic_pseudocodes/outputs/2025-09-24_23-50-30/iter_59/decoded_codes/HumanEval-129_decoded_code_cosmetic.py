from typing import List

def minPath(w: List[List[int]], r: int) -> List[int]:
    s: int = len(w)
    t: int = s * s + 1
    u: int = 0
    while u <= s - 1:
        v: int = 0
        while v <= s - 1:
            if not (w[u][v] == 0):
                x: List[int] = []
                if u != 0:
                    x.append(w[u - 1][v])
                if v != 0:
                    x.append(w[u][v - 1])
                if u != s - 1:
                    x.append(w[u + 1][v])
                if v != s - 1:
                    x.append(w[u][v + 1])
                if x:  # Only update t if x is non-empty
                    t = min(t, min(x))
            v += 1
        u += 1
    y: List[int] = []
    z: int = 0
    while z <= r - 1:
        if (z % 2) == 0:
            y.append(1)
        else:
            y.append(t)
        z += 1
    return y