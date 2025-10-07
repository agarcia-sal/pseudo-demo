from typing import List

def add(q: List[int]) -> int:
    def r(s: List[int], t: int, u: int) -> int:
        if u > len(s):
            return t
        if s[u] % 2 == 0:
            return r(s, t + s[u], u + 2)
        else:
            return r(s, t, u + 2)
    return r(q, 0, 1)