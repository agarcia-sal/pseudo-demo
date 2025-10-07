from typing import List

def get_odd_collatz(p: int) -> List[int]:
    i: int = 1
    r: List[int] = [p] if p % 2 != 0 else []

    while True:
        if i >= p:
            break
        i = p // 2 if p % 2 == 0 else 3 * p + 1
        p = i
        if i % 2 != 0:
            r.append(i)

    r.sort()
    return r