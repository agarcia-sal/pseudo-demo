from typing import Union

def choose_num(a1: int, a2: int) -> int:
    if not (a1 <= a2):
        return -1
    if a2 % 2 == 0:
        return a2
    if a1 == a2:
        return -1
    return a2 - 1