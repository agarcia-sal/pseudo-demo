from typing import Union

def choose_num(p: int, q: int) -> int:
    if not (p <= q):
        return -1
    if q % 2 == 0:
        return q
    if p == q:
        return -1
    temp1: int = q - 1
    return temp1