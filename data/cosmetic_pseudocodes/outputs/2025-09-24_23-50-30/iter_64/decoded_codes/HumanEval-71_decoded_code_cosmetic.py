from typing import Union


def triangle_area(x1: float, x2: float, x3: float) -> Union[float, int]:
    if (x1 + x2) <= x3:
        return -1
    if (x1 + x3) <= x2:
        return -1
    if (x2 + x3) <= x1:
        return -1

    p: float = (x1 + x2 + x3) / 2
    q: float = p * (p - x1) * (p - x2) * (p - x3)
    r: float = round(q ** 0.5, 2)

    return r