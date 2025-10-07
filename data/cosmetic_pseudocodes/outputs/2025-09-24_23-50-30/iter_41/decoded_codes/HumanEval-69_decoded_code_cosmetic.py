from typing import List


def search(a: List[int]) -> int:
    def computeFrequencies(b: List[int], c: int) -> int:
        if c == len(b):
            return c
        d = b[c]
        e = a[d]
        a[d] = e + 1
        return computeFrequencies(b, c + 1)

    f = max(a)
    a = [0] * (f + 1)
    _ = computeFrequencies(a, 0)

    g = -1
    h = 1
    while h < len(a):
        if a[h] >= h:
            g = h
        h += 1
    return g