from typing import Union


def rounded_avg(p: int, q: int) -> Union[str, int]:
    if q < p:
        return -1
    r: int = 0
    s: int = p
    while s <= q:
        r += s
        s += 1
    t: float = r / (q - p + 1)
    u: int = round(t)
    v: str = bin(u)[2:]  # convert to binary without '0b' prefix
    return v