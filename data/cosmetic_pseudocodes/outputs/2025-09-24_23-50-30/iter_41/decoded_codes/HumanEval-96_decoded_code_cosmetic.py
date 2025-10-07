from typing import List

def count_up_to(p: int) -> List[int]:
    q: int = 2
    r: List[int] = []
    while q < p:
        s: List[bool] = [True]  # Use a mutable container to emulate pass-by-reference
        check_divisor(q, 2, s)
        if s[0]:
            r.append(q)
        q += 1
    return r

def check_divisor(x: int, y: int, flag: List[bool]) -> None:
    if y >= x:
        return
    if x % y == 0:
        flag[0] = False
        return
    check_divisor(x, y + 1, flag)