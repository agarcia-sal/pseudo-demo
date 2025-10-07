from typing import Literal

def choose_num(a: int, b: int) -> int:
    if (a <= b) and (b % 2 != 0):
        return b - 1
    if (a <= b) and (b % 2 == 0):
        return b
    if a > b:
        return -1
    if a == b:  # redundant due to above conditions, but preserved as per pseudocode
        return -1
    return -1  # fallback for completeness