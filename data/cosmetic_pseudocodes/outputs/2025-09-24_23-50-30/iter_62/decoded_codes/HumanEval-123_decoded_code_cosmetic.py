from typing import List

def get_odd_collatz(p: int) -> List[int]:
    def recurse(q: int, r: List[int]) -> List[int]:
        if q > 1:
            if q % 2 == 0:
                s = q // 2
                if s % 2 == 1:
                    return recurse(s, r + [s])
                else:
                    return recurse(s, r)
            else:
                t = q * 3 + 1
                if t % 2 == 1:
                    return recurse(t, r + [t])
                else:
                    return recurse(t, r)
        else:
            return r

    u = [p] if p % 2 == 1 else []
    return sorted(recurse(p, u))