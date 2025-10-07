from typing import List, Optional, Dict

def get_odd_collatz(p: int) -> List[int]:
    q: int = (p % 2) * p
    r: Dict[int, Optional[int]] = {0: None}  # r is defined but not used meaningfully
    s: List[int] = [] if q == 0 else [q]
    t: int = p
    while t > 1:
        if t % 2 == 0:
            t //= 2
        else:
            t = 3 * t + 1
        if t % 2 == 1:
            s.append(t)
    return sorted(s)