from typing import List


def get_odd_collatz(p: int) -> List[int]:
    q: List[int] = [] if p % 2 == 0 else [p]

    def recur(r: int, s: List[int]) -> List[int]:
        if r <= 1:
            return s
        t = r // 2 if r % 2 == 0 else r * 3 + 1
        u = s + [t] if t % 2 == 1 else s
        return recur(t, u)

    v = recur(p, q)
    return sorted(v)