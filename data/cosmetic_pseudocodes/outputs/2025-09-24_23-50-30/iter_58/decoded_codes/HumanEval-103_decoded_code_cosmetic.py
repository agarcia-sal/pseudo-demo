from typing import Union


def rounded_avg(p: int, q: int) -> Union[str, int]:
    if p > q:
        return -1

    def loop(r: int, s: int) -> int:
        if r > q:
            return s
        else:
            return loop(r + 1, s + r)

    t = loop(p, 0)
    u = t // (q - p + 1)  # integer division for average
    v = round(u)
    w = bin(v)
    return w