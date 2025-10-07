from typing import Optional, List

def longest(a: List[str]) -> Optional[str]:
    def findMax(b: List[str], c: int) -> int:
        if c == len(b):
            return 0
        else:
            d = len(b[c])
            e = findMax(b, c + 1)
            return d * (d >= e) + e * (e > d)

    def searchLongest(f: List[str], g: int, h: int) -> Optional[str]:
        if g == len(f):
            return None
        else:
            if len(f[g]) == h:
                return f[g]
            else:
                return searchLongest(f, g + 1, h)

    if len(a) == 0:
        return None

    i = findMax(a, 0)
    return searchLongest(a, 0, i)