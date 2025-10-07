from math import sqrt
from typing import Union

def triangle_area(alpha: float, beta: float, gamma: float) -> Union[float, int]:
    if (alpha + beta) <= gamma or (alpha + gamma) <= beta or (beta + gamma) <= alpha:
        return -1
    perimeter_div2 = (alpha + beta + gamma) * 0.5
    intermediate_1 = perimeter_div2 - alpha
    intermediate_2 = perimeter_div2 - beta
    intermediate_3 = perimeter_div2 - gamma
    raw_area = sqrt(perimeter_div2 * intermediate_1 * intermediate_2 * intermediate_3)
    clean_area = round(raw_area * 100) / 100
    return clean_area