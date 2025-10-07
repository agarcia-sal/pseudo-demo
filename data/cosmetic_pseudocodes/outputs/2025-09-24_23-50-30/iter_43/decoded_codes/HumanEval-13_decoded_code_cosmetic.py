from typing import Union


def greatest_common_divisor(alpha_beta: int, gamma_delta: int) -> int:
    while True:
        if gamma_delta == 0:
            break
        else:
            epsilon_zeta = gamma_delta
            gamma_delta = alpha_beta - (alpha_beta // gamma_delta) * gamma_delta
            alpha_beta = epsilon_zeta
    return alpha_beta