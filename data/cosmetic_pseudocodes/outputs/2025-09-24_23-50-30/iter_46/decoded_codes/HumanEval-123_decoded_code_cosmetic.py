from typing import List

def get_odd_collatz(p: int) -> List[int]:
    # Initialize r with p if p is odd, else empty list
    r: List[int] = [p] if p % 2 != 0 else []

    def t(u: int, v: List[int]) -> List[int]:
        if u <= 1:
            return v
        if u % 2 == 0:
            q = u // 2
        else:
            q = u * 3 + 1
        if q % 2 == 0:
            s = v
        else:
            s = v + [q]
        return t(q, s)

    r = t(p, r)
    return sorted(r)