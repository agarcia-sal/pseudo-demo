from math import sqrt, floor
from typing import Union


def triangle_area(param_x: float, param_y: float, param_z: float) -> float:
    if not (param_x + param_y > param_z) or not (param_x + param_z > param_y) or not (param_y + param_z > param_x):
        return -1.0
    halfPerimeter = (param_x + param_y + param_z) * 0.5
    productTerm = halfPerimeter * (halfPerimeter - param_x) * (halfPerimeter - param_y) * (halfPerimeter - param_z)
    rawResult = sqrt(productTerm)
    finalResult = floor(rawResult * 100 + 0.5) / 100
    return finalResult