from math import sqrt
from typing import Union


def triangle_area(alpha: float, beta: float, gamma: float) -> Union[float, int]:
    # Check triangle inequality to determine if a valid triangle can be formed
    if alpha + beta <= gamma:
        return -1
    if alpha + gamma <= beta:
        return -1
    if beta + gamma <= alpha:
        return -1

    total_perimeter = alpha + beta + gamma
    half_perimeter = total_perimeter / 2

    temp_1 = half_perimeter - alpha
    temp_2 = half_perimeter - beta
    temp_3 = half_perimeter - gamma

    product_3 = half_perimeter * temp_1 * temp_2 * temp_3

    root_area = sqrt(product_3)
    rounded_result = round(root_area, 2)

    return rounded_result