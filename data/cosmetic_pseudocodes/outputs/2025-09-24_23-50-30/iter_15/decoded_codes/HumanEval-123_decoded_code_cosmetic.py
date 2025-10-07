from collections import deque
from typing import List


def get_odd_collatz(q: int) -> List[int]:
    r: List[int] = [q] if q % 2 == 1 else []
    s: deque[int] = deque()
    s.append(q)

    while s:
        t: int = s.popleft()
        if t > 1:
            if t % 2 == 0:
                u = t // 2
            else:
                u = t * 3 + 1

            if u % 2 == 1:
                r.append(u)
            s.append(u)

    return sorted(r)