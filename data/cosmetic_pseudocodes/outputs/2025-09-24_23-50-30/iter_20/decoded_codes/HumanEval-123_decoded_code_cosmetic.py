from typing import List

def get_odd_collatz(p: int) -> List[int]:
    q: List[int] = [p] if (p % 2 != 0) else []
    r: int = p
    while r > 1:
        if r % 2 != 0:
            r = r * 3 + 1
        else:
            r //= 2
        if r % 2 == 1:
            q.append(r)
    return sorted(q)