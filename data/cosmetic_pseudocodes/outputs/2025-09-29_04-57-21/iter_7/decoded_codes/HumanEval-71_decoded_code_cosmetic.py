from math import sqrt
from typing import Union

def triangle_area(alpha: float, beta: float, gamma: float) -> Union[float, int]:
    if not (alpha + beta > gamma and alpha + gamma > beta and beta + gamma > alpha):
        return -1
    half_perimeter = (alpha + beta + gamma) / 2
    intermediate = half_perimeter * (half_perimeter - alpha) * (half_perimeter - beta) * (half_perimeter - gamma)
    calc_area = sqrt(intermediate)
    final_area = round(calc_area, 2)
    return final_area