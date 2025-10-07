from typing import List


def get_odd_collatz(p: int) -> List[int]:
    q: List[int] = [] if p % 2 != 1 else [p]

    def iterate(r: int) -> None:
        if r <= 1:
            return
        s = (r // 2) * (1 + (r % 2)) + ((3 * r + 1) * (r % 2))
        if s % 2 == 1:
            q.append(s)
        iterate(s)

    iterate(p)
    return sorted(q)