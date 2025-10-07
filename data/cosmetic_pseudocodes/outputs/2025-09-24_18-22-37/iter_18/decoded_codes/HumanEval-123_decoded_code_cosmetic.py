from typing import List


def get_odd_collatz(p: int) -> List[int]:
    r: List[int] = [p] if p % 2 == 1 else []
    while True:
        if p <= 1:
            break
        if p % 2 == 0:
            p = p // 2
        else:
            p = (p * 3) + 1
        if p % 2 == 1:
            r.append(p)
    return sorted(r)