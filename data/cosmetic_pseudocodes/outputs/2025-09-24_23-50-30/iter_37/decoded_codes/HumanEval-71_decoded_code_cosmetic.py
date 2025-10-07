from math import sqrt
from typing import Union


def triangle_area(x: float, y: float, z: float) -> Union[float, int]:
    if not (x + y > z and x + z > y and y + z > x):
        return -1
    half_perimeter = (x + y + z) / 2
    intermediate_product = half_perimeter * (half_perimeter - x) * (half_perimeter - y) * (half_perimeter - z)
    root_result = sqrt(intermediate_product)
    precise_result = round(root_result, 2)
    return precise_result