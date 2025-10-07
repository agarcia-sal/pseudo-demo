from math import sqrt
from typing import Union


def triangle_area(x: float, y: float, z: float) -> Union[float, int]:
    if not (x + y > z and x + z > y and y + z > x):
        return -1
    s = (x + y + z) / 2
    product = s * (s - x) * (s - y) * (s - z)
    result = round(sqrt(product), 2)
    return result