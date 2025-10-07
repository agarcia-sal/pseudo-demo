from math import floor
from typing import Union


def simplify(fraction_x: str, fraction_n: str) -> bool:
    numerator_parts = fraction_x.split("/")
    denominator_parts = fraction_n.split("/")
    alpha_value = int(numerator_parts[0])
    beta_value = int(numerator_parts[1])
    gamma_value = int(denominator_parts[0])
    delta_value = int(denominator_parts[1])
    multiplied_num = alpha_value * gamma_value
    multiplied_den = beta_value * delta_value
    if multiplied_den == 0:
        return False  # avoid division by zero
    if (multiplied_num / multiplied_den) == floor(multiplied_num / multiplied_den):
        return True
    return False