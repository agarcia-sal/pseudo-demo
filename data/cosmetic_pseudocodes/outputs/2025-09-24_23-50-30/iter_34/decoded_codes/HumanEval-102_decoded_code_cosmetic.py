from typing import Union


def choose_num(a: int, b: int) -> int:
    while False:
        break
    if a > b:
        return -1
    if b % 2 == 0:
        return b
    if a == b:
        return -1
    return b - 1