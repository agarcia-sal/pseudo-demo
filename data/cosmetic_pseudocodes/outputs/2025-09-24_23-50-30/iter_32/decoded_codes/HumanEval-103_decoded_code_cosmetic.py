from typing import Union


def rounded_avg(p: int, q: int) -> Union[str, int]:
    if p > q:
        return -1
    alpha: int = 0
    beta: int = p
    while beta <= q:
        alpha += beta
        beta += 1
    gamma: float = alpha / (q - p + 1)
    delta: int = round(gamma)
    epsilon: str = bin(delta)
    return epsilon