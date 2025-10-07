from typing import Union


def triangle_area(x1: float, x2: float, x3: float) -> Union[float, int]:
    if not (x1 + x2 > x3 and x1 + x3 > x2 and x2 + x3 > x1):
        return -1
    p = (x1 + x2 + x3) / 2
    area_sq = p * (p - x1) * (p - x2) * (p - x3)
    res = round(area_sq**0.5, 2)
    return res