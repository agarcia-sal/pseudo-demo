from typing import Union


def rounded_avg(x1: int, y2: int) -> str:
    if y2 < x1:
        return "-1"
    alpha: int = 0
    beta: int = x1
    while beta <= y2:
        alpha += beta
        beta += 1
    gamma: float = alpha / (y2 - x1 + 1)
    delta: int = round(gamma)
    epsilon: str = bin(delta)[2:]
    return epsilon