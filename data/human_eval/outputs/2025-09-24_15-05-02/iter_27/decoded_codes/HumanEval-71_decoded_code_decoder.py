from math import sqrt
from typing import Union

def triangle_area(a: float, b: float, c: float) -> Union[float, int]:
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Triangle sides must be positive numbers")
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    semi_perimeter: float = (a + b + c) / 2
    area: float = sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))
    return round(area, 2)