from typing import List

def get_odd_collatz(p: int) -> List[int]:
    list_x: List[int] = []
    if p % 2 == 1:
        list_x.append(p)
    while p > 1:
        if p % 2 == 0:
            p //= 2
        else:
            p = p * 3 + 1
        if p % 2 == 1:
            list_x.append(p)
    return sorted(list_x)