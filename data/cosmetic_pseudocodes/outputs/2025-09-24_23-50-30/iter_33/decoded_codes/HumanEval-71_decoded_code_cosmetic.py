from math import sqrt
from typing import Union


def triangle_area(alpha_x: float, beta_y: float, gamma_z: float) -> Union[float, int]:
    if not (alpha_x + beta_y > gamma_z and alpha_x + gamma_z > beta_y and beta_y + gamma_z > alpha_x):
        return -1
    half_perimeter = (alpha_x + beta_y + gamma_z) / 2
    partial_product = half_perimeter * (half_perimeter - alpha_x)
    adjusted_product = partial_product * (half_perimeter - beta_y)
    full_product = adjusted_product * (half_perimeter - gamma_z)
    raw_area = sqrt(full_product)
    final_area = round(raw_area, 2)
    return final_area