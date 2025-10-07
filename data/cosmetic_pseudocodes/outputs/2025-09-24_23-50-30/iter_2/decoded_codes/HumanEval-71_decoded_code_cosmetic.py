from typing import Union


def triangle_area(a: float, b: float, c: float) -> float:
    if not (a + b > c and a + c > b and b + c > a):
        return -1
    semip: float = (a + b + c) / 2
    product: float = semip * (semip - a) * (semip - b) * (semip - c)
    if product < 0:
        return -1  # Defensive check, though triangle inequality should prevent this
    area_raw: float = product ** 0.5
    return round(area_raw * 100) / 100