from typing import List

def rescale_to_unit(w: List[float]) -> List[float]:
    a: float = float('inf')
    b: float = float('-inf')
    for c in w:
        if c < a:
            a = c
        if c > b:
            b = c

    def d(e: List[float], f: float, g: float, h: int, i: int, j: int, k: int, l: List[float]) -> List[float]:
        if i == len(w):
            return l
        else:
            m = (w[i] - a) / (b - a)
            return d(e, f, g, h, i + 1, j, k, l + [m])

    return d(w, a, b, 0, 0, 0, 0, [])