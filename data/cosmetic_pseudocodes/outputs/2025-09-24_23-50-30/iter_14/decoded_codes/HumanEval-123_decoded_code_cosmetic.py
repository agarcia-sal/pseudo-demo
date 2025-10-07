from typing import List

def get_odd_collatz(q: int) -> List[int]:
    r: List[int] = []
    if q % 2 == 1:
        r.append(q)
    s: int = r[0] if r else 0

    while True:
        if s <= 1:
            break
        if s % 2 == 0:
            s //= 2
        else:
            s = 3 * s + 1
        if s % 2 != 0:
            r.append(s)

    return sorted(r)