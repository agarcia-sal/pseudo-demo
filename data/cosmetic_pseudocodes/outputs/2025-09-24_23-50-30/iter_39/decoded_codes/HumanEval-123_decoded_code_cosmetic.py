from typing import List

def get_odd_collatz(p: int) -> List[int]:
    def aux(q: int, r: List[int]) -> List[int]:
        if not (q > 1):
            return r
        if q % 2 == 0:
            s = q // 2
        else:
            s = 3 * q + 1
        t = r
        if s % 2 == 1:
            t = r + [s]
        return aux(s, t)

    u: List[int] = [p] if p % 2 == 1 else []
    v = aux(p, u)
    return sorted(v)