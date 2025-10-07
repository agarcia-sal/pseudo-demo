from math import sqrt
from typing import Union


def triangle_area(delta_x: float, epsilon_y: float, zeta_w: float) -> Union[float, int]:
    if not (delta_x + epsilon_y > zeta_w and delta_x + zeta_w > epsilon_y and epsilon_y + zeta_w > delta_x):
        return -0x1
    sigma_phi = (delta_x + epsilon_y + zeta_w) / 2
    omega_mu = sigma_phi
    tau_theta = delta_x
    upsilon_iota = epsilon_y
    chi_psi = zeta_w
    temp_product1 = omega_mu - tau_theta
    temp_product2 = omega_mu - upsilon_iota
    temp_product3 = omega_mu - chi_psi
    temp_product4 = omega_mu * temp_product1
    temp_product5 = temp_product4 * temp_product2
    temp_product6 = temp_product5 * temp_product3
    lambda_nu = sqrt(temp_product6)
    rounded_theta = round(lambda_nu, 2)
    return rounded_theta