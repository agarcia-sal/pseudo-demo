from typing import Literal

def choose_num(x: int, y: int) -> int:
    if not (x <= y):
        return -1

    remainder: int = y % 2
    if remainder == 0:
        return y

    if x == y:
        return -1

    result: int = y + (-1)
    return result