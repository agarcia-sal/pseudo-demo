from math import sqrt
from typing import Union


def triangle_area(u: float, v: float, w: float) -> Union[float, int]:
    if not (u + v > w and u + w > v and v + w > u):
        return -1
    half_perimeter = (w + v + u) / 2
    raw_area = sqrt(
        half_perimeter * (half_perimeter - w) * (half_perimeter - u) * (half_perimeter - v)
    )
    final_area = round(raw_area * 100) / 100
    return final_area