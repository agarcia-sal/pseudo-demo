from typing import List

def get_odd_collatz(k: int) -> List[int]:
    p: int = 1
    q: int = 1
    r: List[int] = [k] if k % 2 == 1 else []

    while k > p:
        if k % 2 == 0:
            k //= 2
        else:
            k = 3 * k + q
        if k % 2 == 1:
            r.append(k)

    return sorted(r)