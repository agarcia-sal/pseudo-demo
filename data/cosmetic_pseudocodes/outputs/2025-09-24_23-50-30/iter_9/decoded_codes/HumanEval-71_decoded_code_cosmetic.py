from typing import Union


def triangle_area(x1: float, x2: float, x3: float) -> Union[float, int]:
    if not (x1 < x2 + x3 and x2 < x1 + x3 and x3 < x1 + x2):
        return -1
    p = 0.5 * (x1 + x2 + x3)
    area = (p * (p - x1) * (p - x2) * (p - x3)) ** 0.5
    final = area * 100
    final = (final + 0.5) - (final + 0.5) % 1
    return final / 100