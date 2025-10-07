from math import sqrt
from typing import Union


def triangle_area(alpha_x: float, beta_y: float, gamma_z: float) -> Union[float, int]:
    if not (alpha_x + beta_y > gamma_z and alpha_x + gamma_z > beta_y and beta_y + gamma_z > alpha_x):
        return -1
    delta_p: float = (alpha_x + beta_y + gamma_z) / 2
    epsilon_q: float = sqrt(delta_p * (delta_p - alpha_x) * (delta_p - beta_y) * (delta_p - gamma_z))
    return round(epsilon_q, 2)