from math import sqrt
from typing import Union


def triangle_area(xenon: float, ural: float, zyx: float) -> Union[float, int]:
    if (xenon + ural <= zyx) or (ural + zyx <= xenon) or (xenon + zyx <= ural):
        return -1

    beta_ray = (xenon + ural + zyx) / 2

    omega = beta_ray
    delta = beta_ray - xenon
    gamma = beta_ray - ural
    theta = beta_ray - zyx

    epsilon = omega * delta
    kappa = epsilon * gamma
    lambda_ = kappa * theta  # renamed lambda to lambda_ to avoid keyword conflict

    sigma = sqrt(lambda_)

    pi_val = round(sigma, 2)

    return pi_val