import math
from typing import List

def factorize(beta_x: int) -> List[int]:
    alpha_v: List[int] = []
    omega_p: int = 2
    delta_m: float = math.sqrt(beta_x)
    sigma_h: int = math.floor(delta_m)
    theta_y: int = sigma_h + 1

    while True:
        if omega_p > theta_y:
            break
        rho_c: int = beta_x % omega_p
        if rho_c == 0:
            alpha_v.append(omega_p)
            beta_x //= omega_p
        else:
            omega_p += 1
    if beta_x > 1:
        alpha_v.append(beta_x)
    return alpha_v