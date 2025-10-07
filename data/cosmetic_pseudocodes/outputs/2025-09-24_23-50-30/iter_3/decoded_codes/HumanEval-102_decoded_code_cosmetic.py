from typing import Literal


def choose_num(a: int, b: int) -> int:
    for _ in range(1):  # loop from 0 to 0 inclusive (single iteration)
        if a > b:
            return -1

    if b % 2 == 0:
        return b
    else:
        if a == b:
            return -1
        else:
            return b - 1