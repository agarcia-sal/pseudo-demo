from typing import List

def get_odd_collatz(q: int) -> List[int]:
    w: List[int] = [q] if q % 2 == 1 and q > 0 else []
    while q > 1:
        if q % 2 == 0:
            q = q // 2
        else:
            q = 3 * q + 1
            w.append(q)
    return sorted(w)